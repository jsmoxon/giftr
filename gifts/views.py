from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from gifts.models import *
from gifts.forms import RecipientForm, AddGiftFormset, SignupForm, AddGiftOptionAdminForm, ConfirmGiftChoiceForm, AddRecipientFormset
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
import os

def index(request):
	return HttpResponse("This is the home page of Giftr!")

def signup_for_account(request):
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			email = form.cleaned_data['email']
			user = User.objects.create_user(username, email, password)
			user.save()
			UserProfile.objects.create(user=user)
			authorize_user = authenticate(username=username, password=password)
			if authorize_user is not None:
				if authorize_user.is_active:
					login(request, authorize_user)
				else: 
					print "User is not active."
			else:
				print "No user in database."
			return redirect('add_recipient')
		else:
			return render(request, 'signup.html', {'form':form})
	else:
		form = SignupForm()
	return render(request, 'signup.html', {'form':form})

@login_required
def add_recipient(request):
	user_profile = UserProfile.objects.get(user=request.user)	
	if request.method == "POST":
		form = RecipientForm(request.POST)
		formset = AddGiftFormset(request.POST)
		if form.is_valid() and formset.is_valid():
			recipient = form.save_form(user_profile)
			formset.save_formset(recipient, user_profile)
			return redirect('dashboard')
		else:
			render(request, 'add_recipient.html', {'form':form, 'formset':formset})
	else:
		form = RecipientForm()
		formset= AddGiftFormset()
	return render(request, 'add_recipient.html', {'form':form, 'formset':formset})

@login_required
def dashboard(request):
	user_profile = UserProfile.objects.get(user=request.user)	
	recipients = Recipient.objects.filter(user=user_profile)
	gifts = {}
	for recipient in recipients:
		if Gift.objects.filter(recipient=recipient):
			gifts[recipient] = (Gift.objects.filter(recipient=recipient))
	return render(request, 'dashboard.html', {'recipients':recipients, 'gifts':gifts, 'user':user_profile})

@login_required
def occasion_page(request, gift_id):
	user_profile = UserProfile.objects.get(user=request.user)	
	gift = Gift.objects.get(pk=gift_id)
	if gift.recipient.user == user_profile or user_profile.user.is_staff:
		return render(request, 'occasion_page.html', {'gift':gift})
	else:
		print "user is not staff or related to the recipient"
		return render(request, "login.html")
	

@login_required()
def occasion_gift_confirmation_page(request, gift_id, gift_option_id):
	"""this view allows a user to confirm that they want to buy a certain gift, add a note and 
	ship to address; in the short term we may replace it with a direct link to purchase the item"""
	user_profile = UserProfile.objects.get(user=request.user)	
	gift = Gift.objects.get(pk=gift_id)	
	gift_choice = GiftOption.objects.get(pk=gift_option_id)
	if request.method == "POST":
		form = ConfirmGiftChoiceForm(request.POST)
		if form.is_valid():
			form.save_form(gift, gift_choice)
			#note we are hardcoding gift status here, I know it's terrible but we'll come back to it
			status = GiftStatus.objects.filter(value="buying")
			print status[0]
			gift.status = status[0]
			gift.gift_selected = gift_choice
			gift.save()
			return HttpResponse("Your gift will be sent!")
		else:
			return HttpResponse("this form aint vaild!")	
	else:
		#does this need to be added for POST requests too? 
		if gift.recipient.user == user_profile or user_profile.user.is_staff:
			form = ConfirmGiftChoiceForm()
		else:
			return render(request, "404.html")
	return render(request, 'confirm_choice.html', {'gift':gift, 'gift_choice':gift_choice,'form':form})

# I don't think we'll use this view; will just use Django admin
@login_required
def create_product(request):
	if request.method == "POST":
		form = AddGiftOptionAdminForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
		else:
			HttpResponse("This form is not valid yo!")
	else:
		form = AddGiftOptionAdminForm()
	return render(request, 'create_product.html', {'form':form})

#PK what does this do? I don't think we need it.
def header(request):
	return render(request, 'header.html')

OPTION_EMAIL_BASE_URL = os.environ.get('OPTION_EMAIL_BASE_URL', '')

@login_required
def send_occasion_email(request, gift_id, user_id):
	"""this view allows an admin to auto send an email with gift options to a user_profile automatically;
	note the hardcoding and lack of safety checks i.e. you could send an email before populating gift options 
	if you aren't careful"""
	user_profile = UserProfile.objects.get(user=request.user)	
	if user_profile.user.is_staff:
		gift = Gift.objects.get(pk=gift_id)
		recipient = gift.recipient.name
		occasion_page_url = OPTION_EMAIL_BASE_URL+"/gifts/occasion/"+str(gift.id)
#		occasion_page_url = "http://127.0.0.1:8000/gifts/occasion/%s" % gift_id
		subject = "Gift options for "+str(recipient)
		message = "Here are 3 gift options: %s \n\n Click the link to choose one and we'll take care of the rest! \n\nIf you don't like any of them just reply to this email and we'll help you find something better. \n\nThe Team" % str(occasion_page_url)
		from_email = "trygiftrapp@gmail.com"
		to_email = [UserProfile.objects.get(pk=user_id).user.email]
		send_mail(subject, message, from_email, to_email, fail_silently=False)
		#note hardcoding status
		gift.status = GiftStatus.objects.filter(value="awaiting on a reply from you")[0]
		gift.save()
	else:
		return HttpResponse("Requester is not an admin.")
	return redirect('/admin/gifts/gift/')










