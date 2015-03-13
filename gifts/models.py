from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	"""primary user profile info"""
	user = models.ForeignKey(User, unique=True)

	def __unicode__(self):
		return str(self.user)

class Recipient(models.Model):
	"""docstring for ClassName"""
	user = models.ForeignKey(UserProfile, null=True, blank=True)
	name = models.CharField(max_length=1000, null=True, blank=True)
	birthday = models.DateField(null=True, blank=True)
	address = models.TextField(null=True, blank=True)
	notes = models.TextField(null=True, blank=True)
	favorites = models.TextField(null=True, blank=True)
	#need to make gender choices...
	gender = models.CharField(max_length=10, null=True, blank=True)

	def __unicode__(self):
		return str(self.name+" - "+self.user.user.username)
		

class GiftOption(models.Model):
	url = models.URLField(max_length=200, null=True, blank=True)
	#active means that it's a choice that the user is still considering
	active = models.BooleanField(default=True)
	#selected is shows that the gift has been chosen by the user to be sent
	selected = models.BooleanField(default=False)
	name = models.CharField(max_length=1000, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	photo_url = models.URLField(max_length=300, null=True, blank=True)
	notes = models.TextField(null=True, blank=True)
	price = models.IntegerField(null=True, blank=True)
	def __unicode__(self):
		return str(self.name)

class GiftStatus(models.Model):
	value = models.CharField(max_length=1000, null=True, blank=True)
	def __unicode__(self):
		return str(self.value)	

class Gift(models.Model):
	recipient = models.ForeignKey(Recipient)
	occasion = models.CharField(max_length=1000, null=True, blank=True)
	gift_options = models.ManyToManyField(GiftOption, blank=True, null=True)
	#gift_selected = filter the gift options to find the selected gift
	occasion_date = models.DateField(null=True, blank=True)
	send_gift_option_email_date = models.DateField(null=True, blank=True) 	
	start_process_date = models.DateField(auto_now_add=True)
	ship_to_address = models.TextField(null=True, blank=True)
	status = models.ForeignKey(GiftStatus, null=True, blank=True)

	def __unicode__(self):
		return str(self.recipient.name+" - "+self.occasion)




