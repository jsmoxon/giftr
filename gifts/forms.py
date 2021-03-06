from django.forms import ModelForm, PasswordInput, HiddenInput, TextInput, Textarea, Select, CheckboxSelectMultiple, DateInput, DateField, CharField, ModelMultipleChoiceField, EmailField
from gifts.models import *
from django.forms.formsets import formset_factory, BaseFormSet
import datetime
import os

class SignupForm(ModelForm):
	"""Form for signing up a user"""
	email = CharField(required=True, widget=TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = User
		fields = ('email', 'password', 'first_name')
		widgets = {
			'password': PasswordInput(attrs={'class':'form-control', 'cols':2}),
			'email': TextInput(attrs={'class':'form-control'}),
			'first_name': TextInput(attrs={'class':'form-control'}),
		}

		labels = {
			'first_name': "First Name (optional):"
		}

class BetaSignupForm(ModelForm):
	email = EmailField(required=True, label='', widget=TextInput(attrs={'class':'form-control', 'placeholder':'Enter email'},))
	class Meta:
		model = BetaSignup
		fields = ('email',)		
		widgets = {
			'email': TextInput(attrs={'class':'form-control'}),		
		}
		labels = {
			'email':'',
		}

#idea here is to add multiple recipients at once...will revisit when time
class BaseRecipientForm(BaseFormSet):
	def save_formset(self, user_profile, formset_function):
		for form in self.forms:
			try:
				 recipient = Recipient.objects.create(
					user=user_profile,
					name=self.cleaned_data['name'],
					birthday=self.cleaned_data['birthday'],
					address=self.cleaned_data['address'],				
					favorites=self.cleaned_data['favorites'],
					gender=self.cleaned_data['gender']
					)
				 recipient.save()
				 print "Just save the recipient "+str(recipient)
				 formset_function(recipient)
				 print "just called formset_function"
			except:
				pass

#not using any more can delete
FAVORITE_CHOICES = (
	('Books', (
		('Mysteries & Thrillers','Mysteries & Thrillers'),
		('Bios & Memoirs','Bios & Memoirs'),
		('Best sellers','Best sellers'),
		('Sci Fi & Fantasy','Sci Fi & Fantasy'),
		('Self Development','Self Development'),
		('Nonfiction','Nonfiction'),
		('Romance','Romance'),
		)
	),
	('Activites', (
		('Ball Sports','Ball Sports'),
		('Outdoors','Outdoors'),
		('Games','Games'),
		('Travel','Travel'),
		('Cycling','Cycling'),
		('Running','Running'),
		('Golf','Golf'),		
		)
	),
	('Art', (
		('Movies','Movies'),
		('Prints','Prints'),
		('Music','Music'),
		)
	),
	('Home', (
		('Kitchen','Kitchen'),
		('Backyard','Backyard'),
		('General (fun)','General (fun)'),
		('General (useful)','General (useful)'),
		('Bath & Body','Bath & Body'),
		)
	),	
	('Personal', (
		('Belts and Accesseries','Belts and Accesseries'),
		('Technology','Technology'),
		('Jewlery','Jewlery'),
		)
	),	
	('Experiences', (
		('Weekend away','Weekend away'),
		('Adventure','Adventure'),
		('In the city','In the city'),
		('Relaxation or Pamper','Relaxation or Pamper'),
		('Educational or Invigorating','Educational or Invigorating'),
		)
	),					
)

def generate_favorite_choices():
	meta_categories = FavoriteTagMetaCategory.objects.all()
	choices = []
	for category in meta_categories:
		if category.active == True:
			choices_two = []
			for tag in category.favoritetag_set.all():
				if tag.active == True:
					choices_two.append([str(tag.name), str(tag.name)])
			choices.append([str(category.name), choices_two])
	return choices

GENDER_CHOICES = (
	('female', 'Female'),
	('male', 'Male'),
	('other', 'Other')
	)

class RecipientForm(ModelForm):
	"""Form for adding a friend or Recipient"""
	name = CharField(required=True, widget=TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = Recipient
		fields = ['name', 'favorites_free_text', 'gender', 'favorites']
		labels = {
			'name': "What is your friend's name?",
			'favorites': "What are some of their favorite hobbies? (Optional)",
			'gender': "What is your friend's gender (Optional)",
			'favorites_free_text': "Anything else we should know about them?",
		}
		widgets = {
			'gender': Select(choices=GENDER_CHOICES,attrs={'class':'form-control'}),
			'favorites': CheckboxSelectMultiple(choices=generate_favorite_choices(), attrs={'class':'test', 'rows':4}),
			'favorites_free_text': Textarea(attrs={'class':'form-control', 'rows':3}),
		}
	def save_form(self,user_profile):
		recipient = Recipient.objects.create(
			user=user_profile,
			name=self.cleaned_data['name'],
			#birthday=self.cleaned_data['birthday'],
			#address=self.cleaned_data['address'],				
			favorites=self.cleaned_data['favorites'],
			favorites_free_text=self.cleaned_data['favorites_free_text'],
			gender=self.cleaned_data['gender'],
		)		
		recipient.save()
		#translates favorites strings into favorite tag objects and stores them
		for tag in self.cleaned_data['favorites'].split("'"):
			fave_tags = FavoriteTag.objects.filter(name=str(tag))
			for fave_tag in fave_tags:
				recipient.favorite_tags.add(fave_tag)
		return recipient

#idea here is to add multiple recipients at once...will revisit when time
AddRecipientFormset = formset_factory(RecipientForm, formset=BaseRecipientForm, extra=5)


def calculate_send_gift_option_email_date(date, days):
	"""calculates when we send them their gift options"""	
	try:
		reminder_date = date + datetime.timedelta(days=days)
		print reminder_date
		return reminder_date
	except:
		print "No occasion date given"

OPTION_EMAIL_BASE_URL = os.environ.get('OPTION_EMAIL_BASE_URL', '')


class BaseAddGiftForm(BaseFormSet):
	"""allows you to add gifts for recipients"""
	def save_formset(self, recipient, user_profile):
		gift_ids = []
		for form in self.forms:
			#hardcode
			status = GiftStatus.objects.get(value="searching for")
			gift = Gift.objects.create(
					recipient = recipient,
					occasion = form.cleaned_data['occasion'],
					occasion_date = form.cleaned_data['occasion_date'],
					send_gift_option_email_date=calculate_send_gift_option_email_date(form.cleaned_data['occasion_date'], -21),
					price_cap=form.cleaned_data['price_cap'],
					status=status
					)
			gift.save()
			#very hacky hardcoding to create an easily accessible url to auto send an email
			gift.admin_send_gift_option_email_url=OPTION_EMAIL_BASE_URL+"/gifts/send_occasion_email/"+str(user_profile.id)+"/"+str(gift.id)
			gift.save()
			gift_ids.append(gift.id)
		return gift_ids

PRICE_CHOICES = (
	('15','Up to $15'),
	('25', 'Up to $25'),
	('50', 'Up to $50'),
	('100', 'Up to $100')
	)

class AddGiftForm(ModelForm):
	occasion_date = DateField(required=True, widget=DateInput(attrs={'class':'datepicker form-control'}))
	class Meta:
		model = Gift
		fields = ['occasion', 'occasion_date', 'price_cap']
		widgets = {
			'price_cap': Select(choices=PRICE_CHOICES,attrs={'class':'form-control'}),
			'occasion': TextInput(attrs={'class':'form-control'}),

		}
		labels = {
			'price_cap': "What is the most you want to spend?",
			'occasion': "What is the occasion? (e.g. Birthday) (Optional)",
			'occasion_date': "By what date do you want the gift to arrive?"
		}

AddGiftFormset = formset_factory(AddGiftForm, formset=BaseAddGiftForm, extra=1)

#forms for admins looking to add products and create occassion pages; not currently used

class AddGiftOptionAdminForm(ModelForm):
	class Meta:
			model = GiftOption
			exclude = ['selected', 'active']

class ConfirmGiftChoiceForm(ModelForm):
	class Meta:
		model = Gift
		fields = ['ship_to_address', 'gift_selected' , 'note_to_recipient']
		widgets = {
			'gift_selected': HiddenInput(),
			'ship_to_address': Textarea(attrs={'class':'form-control', 'cols': 10, 'rows': 4}),
			'note_to_recipient': Textarea(attrs={'class':'form-control', 'cols': 10, 'rows': 4}),

		}
	def save_form(self, gift, gift_choice):
		gift = gift
		gift.ship_to_address = self.cleaned_data['ship_to_address']
		gift.gift_selected = self.cleaned_data['gift_selected']
		gift.note_to_recipient = self.cleaned_data['note_to_recipient']
		gift.save()













