from django.contrib import admin
from gifts.models import *

admin.site.register(UserProfile)

class RecipientAdmin(admin.ModelAdmin):
	list_display = ['name','user', 'birthday']

admin.site.register(Recipient, RecipientAdmin)

class GiftAdmin(admin.ModelAdmin):
	list_display = ['id', 'recipient', 'occasion', 'occasion_date', 'send_gift_option_email_date', 'admin_send_gift_option_email_url', 'status', 'gift_selected']
	list_filter = ['occasion_date','send_gift_option_email_date', 'status']

admin.site.register(Gift, GiftAdmin)

class GiftOptionAdmin(admin.ModelAdmin):
	list_display = ['name', 'id', 'url','price']


admin.site.register(GiftOption, GiftOptionAdmin)
admin.site.register(GiftStatus)
