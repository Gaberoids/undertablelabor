from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from contact_services.models import ContactMessage

# from django_countries.fields import CountryField


class OrderedMessages(models.Model):
    """
    A model to store messages sent
    from user to service provider
    """
    s_order_number = models.CharField(max_length=32, null=False, editable=False)

    s_contact_message = models.ForeignKey(ContactMessage, null=False, blank=False, on_delete=models.CASCADE)

    s_title = models.CharField(max_length=80,
                                    null=True, blank=True)

    s_created_date = models.DateTimeField(auto_now_add=True)

    s_sender = models.ForeignKey(ContactMessage, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='s_sender_username')

    s_receiver = models.ForeignKey(ContactMessage, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='s_receiver_username')
    s_order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    # overwritting default save method
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.s_order_number:
            self.s_order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.s_order_number
