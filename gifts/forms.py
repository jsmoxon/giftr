from django.forms import ModelForm, PasswordInput
from gifts.models import Recipient, Gift, User, GiftStatus
from django.forms.formsets import formset_factory, BaseFormSet
import datetime

class SignupForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		widgets = {
			'password': PasswordInput()
		}

class RecipientForm(ModelForm):
	class Meta:
		model = Recipient
		exclude = ['user']
	def save_form(self,user_profile):
		recipient = Recipient.objects.create(
			user=user_profile,
			name=self.cleaned_data['name'],
			birthday=self.cleaned_data['birthday'],
			address=self.cleaned_data['address'],				
			favorites=self.cleaned_data['favorites'],
			gender=self.cleaned_data['gender'],
		)		
		recipient.save()	
		return recipient

def calculate_send_gift_option_email_date(date, days):
	reminder_date = date + datetime.timedelta(days=days)
	print reminder_date
	return reminder_date

class BaseAddGiftForm(BaseFormSet):
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
		fields = ['occasion', 'occasion_date']

AddGiftFormset = formset_factory(AddGiftForm, formset=BaseAddGiftForm, extra=2)
