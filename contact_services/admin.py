# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import ContactMessage

# classes below will be used to display the data on the client side
class AllMessagesAdmin(admin.ModelAdmin):
    list_display = (
        'm_title',
        'm_body',
        'm_sender_email',
        'm_share_email_box',
        'm_created_date',
        'm_sender',
        'm_receiver',
        'm_sent',
    )
    ordering = ('id',)

admin.site.register(ContactMessage, AllMessagesAdmin)
