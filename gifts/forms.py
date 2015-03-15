from django.forms import ModelForm, PasswordInput, HiddenInput, TextInput
from gifts.models import Recipient, Gift, User, GiftStatus, GiftOption
from django.forms.formsets import formset_factory, BaseFormSet
import datetime

class SignupForm(ModelForm):
	"""Form for signing up a user"""
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		widgets = {
			'password': PasswordInput()
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


class RecipientForm(ModelForm):
	"""Form for adding a friend or Recipient"""
	class Meta:
		model = Recipient
		fields = ['name', 'favorites', 'gender']
		labels = {
			'name': "What is your friend's name?",
			'favorites': "What are some of their favorite hobbies?",
		}
	def save_form(self,user_profile):
		recipient = Recipient.objects.create(
			user=user_profile,
			name=self.cleaned_data['name'],
#			birthday=self.cleaned_data['birthday'],
#			address=self.cleaned_data['address'],				
#			favorites=self.cleaned_data['favorites'],
#			gender=self.cleaned_data['gender'],
		)		
		recipient.save()	
		return recipient

#idea here is to add multiple recipients at once...will revisit when time
AddRecipientFormset = formset_factory(RecipientForm, formset=BaseRecipientForm, extra=5)


def calculate_send_gift_option_email_date(date, days):
	"""calculates when we send them their gift options"""	
	reminder_date = date + datetime.timedelta(days=days)
	print reminder_date
	return reminder_date

class BaseAddGiftForm(BaseFormSet):
	"""allows you to add gifts for recipients"""
	def save_formset(self, recipient):
		for form in self.forms:
			try:
				status = GiftStatus.objects.get(value="Open")
				gift = Gift.objects.create(
					recipient = recipient,
					occasion = form.cleaned_data['occasion'],
					occasion_date = form.cleaned_data['occasion_date'],
					send_gift_option_email_date=calculate_send_gift_option_email_date(form.cleaned_data['occasion_date'], -21),
					status=status
					)
				gift.save()
			except:
				pass

class AddGiftForm(ModelForm):
	class Meta:
		model = Gift
		fields = ['occasion', 'occasion_date', 'price_cap']
		widgets = {
			'occasion_date': TextInput(attrs={'class':'datepicker'})
		}
		labels = {
			'price_cap': "What is the max you want to spend?",
			'occasion': "What is the occasion? (e.g. Birthday)",
			'occasion_date': "By what date do you want the gift to arrive?"
		}

AddGiftFormset = formset_factory(AddGiftForm, formset=BaseAddGiftForm, extra=1)

#forms for admins looking to add products and create occassion pages

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
		}
	def save_form(self, gift, gift_choice):
		gift = gift
		gift.ship_to_address = self.cleaned_data['ship_to_address']
		gift.gift_selected = self.cleaned_data['gift_selected']
		gift.note_to_recipient = self.cleaned_data['note_to_recipient']
		gift.save()













