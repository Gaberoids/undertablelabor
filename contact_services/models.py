from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile

# from django_countries.fields import CountryField


class ContactMessage(models.Model):
    """
    A model to store messages sent
    from user to service provider
    """
    # m_id = models.CharField(max_length=32, null=False, editable=False)

    m_title = models.CharField(max_length=80,
                                    null=True, blank=True)
    m_body = models.CharField(max_length=50,
                                            null=True, blank=True)
    # m_sender_email = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
    #                                  null=True, blank=True, related_name='user')
    m_share_email_box = models.BooleanField(default=False, 
                                                    null=True, blank=True)
    m_created_date = models.DateTimeField(auto_now_add=True)

    m_sender =  models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='m_sender_username')

    m_receiver = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='m_receiver_username')

    # def _generate_m_id(self):
    #     """
    #     Generate a random, unique order number using UUID
    #     """
    #     return uuid.uuid4().hex.upper()

    # method to return the user name
    def __int__(self):
        # print(self) = test2 = user loggedin
        return id

# Create user or save update user information
# @receiver(post_save, sender=User)
# def create_contact_message(sender, instance, created, **kwargs):
#     """
#     Create or update the user profile
#     """
#     if created:
#         ContactMessage.objects.create(user=instance)
    # Existing users: just save the profile
    # instance.userprofile.save()
# 