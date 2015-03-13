from django.contrib import admin
from gifts.models import *

admin.site.register(UserProfile)

class RecipientAdmin(admin.ModelAdmin):
	list_display = ['name','user', 'birthday']

admin.site.register(Recipient, RecipientAdmin)

class GiftAdmin(admin.ModelAdmin):
	list_display = ['recipient', 'occasion_date', 'send_gift_option_email_date']
	list_filter = ['occasion_date','send_gift_option_email_date', 'status']

admin.site.register(Gift, GiftAdmin)

admin.site.register(GiftStatus)
admin.site.register(GiftOption)
