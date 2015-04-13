from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	"""primary user profile info"""
	user = models.ForeignKey(User, unique=True)
	active_beta = models.NullBooleanField(default=False, blank=True, null=True)
	def __unicode__(self):
		return str(self.user)

class BetaSignup(models.Model):
	email = models.EmailField(max_length=254, blank=True, null=True)
	#this doesn't seem to be working on heroku or locally...
	create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	def __unicode__(self):
		return str(self.email)

class FavoriteTagMetaCategory(models.Model):
	"""larger categories for tags, for example Books or Activites rather than Mystery Novels and Hot Air Balloon Rides"""
	name = models.CharField(max_length=1000, null=True, blank=True)
	active = models.BooleanField(default=True)
	def __unicode__(self):
		return str(self.name)

class FavoriteTag(models.Model):
	"""tags for favorites"""
	name = models.CharField(max_length=1000, null=True, blank=True)
	category = models.ForeignKey(FavoriteTagMetaCategory, null=True, blank=True)
	active = models.BooleanField(default=True)
	def __unicode__(self):
		return str(self.category)+"-"+str(self.name)


class Recipient(models.Model):
	"""basically a friend of the user that they want to buy gifts for"""
	user = models.ForeignKey(UserProfile, null=True, blank=True)
	name = models.CharField(max_length=1000, null=True, blank=True)
	birthday = models.DateField(null=True, blank=True)
	address = models.TextField(null=True, blank=True)
	notes = models.TextField(null=True, blank=True)
	favorites = models.TextField(null=True, blank=True)
	favorites_free_text = models.TextField(null=True, blank=True)
	#need to make gender choices...
	gender = models.CharField(max_length=10, null=True, blank=True)
	favorite_tags = models.ManyToManyField(FavoriteTag, blank=True, null=True)
	def __unicode__(self):
		return str("Recipient: "+self.name+" - "+"Giver: "+self.user.user.username+" ")+str(self.id)
		

class GiftOption(models.Model):
	"""This should be thought of as a Product that is one of the options that a UserProfile can purchase as a Gift for their Recipient.
	"""
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
	favorite_tags = models.ManyToManyField(FavoriteTag, blank=True, null=True)

	def __unicode__(self):
		return str(self.name) + " - " + str(self.id)

class GiftStatus(models.Model):
	value = models.CharField(max_length=1000, null=True, blank=True)
	def __unicode__(self):
		return str(self.value)	

class Gift(models.Model):
	#fields for creating an occasion object
	recipient = models.ForeignKey(Recipient)
	occasion = models.CharField(max_length=1000, null=True, blank=True)
	gift_options = models.ManyToManyField(GiftOption, blank=True, null=True)
	gift_selected = models.ForeignKey(GiftOption, blank=True, null=True, related_name="selected_gift_option")
	occasion_date = models.DateField(null=True, blank=True)
	send_gift_option_email_date = models.DateField(null=True, blank=True) 	
	start_process_date = models.DateField(auto_now_add=True)
	ship_to_address = models.TextField(null=True, blank=True)
	status = models.ForeignKey(GiftStatus, null=True, blank=True)
	price_cap = models.IntegerField(null=True, blank=True)
	note_to_recipient = models.TextField(null=True, blank=True)
	admin_send_gift_option_email_url = models.URLField(blank=True, null=True)

	def add_options_by_tag(self, favorite_tags):
		for tag in favorite_tags:
			options = GiftOption.objects.filter(favorite_tags=tag)
			for option in options:
				self.gift_options.add(option)

	def check_if_gift_options_present(self):
		if len(self.gift_options.all()) == 0:
			return False
		else:
			return True

	def __unicode__(self):
		return str(self.recipient.name+" - "+self.occasion)




