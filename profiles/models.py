from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    # one user can only have one profile and vice verse
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Shipping info attached to profile
    default_aka = models.CharField(max_length=80,
                                    null=True, blank=True,
                                    verbose_name="Preferred Name")
    default_service_provider = models.BooleanField(default=False,
                                                    null=True, blank=True,
                                                    verbose_name='Are you a service provider?')
    default_service = models.CharField(max_length=50,
                                            null=True, blank=True, verbose_name="Name the service or the type of work you do")
    default_service_details = models.CharField(max_length=400,
                                            null=True, blank=True, verbose_name='Service or worker details')
    default_town_or_city = models.CharField(max_length=50,
                                            null=True, blank=True, verbose_name='Town or city')
    default_county = models.CharField(max_length=90,
                                      null=True, blank=True, verbose_name='County')
    default_postcode = models.CharField(max_length=20,
                                        null=True, blank=True, verbose_name='Postal Code')

    # method to return the user name
    def __str__(self):
        # print(self.user) = test2 = user loggedin
        return self.user.username


# Create user or save update user information
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
