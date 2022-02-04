from django.contrib import admin

# Register your models here.
from .models import ContactMessage

# classes below will be used to display the data on the client side
class SentMessagesAdmin(admin.ModelAdmin):
    list_display = (
        's_order_number',
        's_contact_message',
        's_title',
        'm_share_email_box',
        's_created_date',
        's_sender',
        's_receiver',
        's_order_total',
    )
    ordering = ('s_order_number',)

admin.site.register(OrderedMessages, OrderedMessagesAdmin)
