from django.contrib import admin

# Register your models here.
from .models import ContactMessage

# classes below will be used to display the data on the client side
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'm_title',
        'm_body',
        'm_share_email_box',
        'm_created_date',
        'm_sender',
        'm_receiver',
    )

    ordering = ('id',)

admin.site.register(ContactMessage, ContactMessageAdmin)
