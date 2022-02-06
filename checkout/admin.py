from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import OrderedMessages

# classes below will be used to display the data on the client side
class OrderedMessagesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        's_order_number',
        's_contact_message',
        's_title',
        's_created_date',
        's_sender',
        's_receiver',
        's_order_total',
    )
    ordering = ('id',)

admin.site.register(OrderedMessages, OrderedMessagesAdmin)