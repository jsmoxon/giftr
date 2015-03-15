from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from gifts.models import *
from gifts.forms import RecipientForm, AddGiftFormset, SignupForm, AddGiftOptionAdminForm, ConfirmGiftChoiceForm, AddRecipientFormset
from django.contrib.auth import authenticate, login

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
			return HttpResponse("Form is not valid.")
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
			formset.save_formset(recipient)
			return redirect('dashboard')
		else:
			HttpResponse("form failed")
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
	gift = Gift.objects.get(pk=gift_id)
	return render (request, 'occasion_page.html', {'gift':gift})

@login_required
def occasion_gift_confirmation_page(request, gift_id, gift_option_id):
	gift = Gift.objects.get(pk=gift_id)	
	gift_choice = GiftOption.objects.get(pk=gift_option_id)
	if request.method == "POST":
		form = ConfirmGiftChoiceForm(request.POST)
		if form.is_valid():
			form.save_form(gift, gift_choice)
			#note we are hardcoding gift status here, I know it's terrible but we'll come back to it
			status = GiftStatus.objects.filter(value="Needs buying")
			print status[0]
			gift.status = status[0]
			gift.gift_selected = gift_choice
			gift.save()
			return HttpResponse("Your gift will be sent!")
		else:
			return HttpResponse("this form aint vaild!")	
	else:
		form = ConfirmGiftChoiceForm()
	return render(request, 'confirm_choice.html', {'gift':gift, 'gift_choice':gift_choice,'form':form})


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


def header(request):
	return render(request, 'header.html')


