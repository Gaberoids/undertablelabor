from django import forms
from .models import ContactMessage


class MessageToServiceForm(forms.ModelForm):
    print("inside form---------***********-----------------**************------------")

    class Meta:
        print("Inside form meta class---------***********-----------------**************------------")
        model = ContactMessage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        print("inside __init___ of form---------***********-----------------**************------------")

        """
        form to send message from user to
        service provider
        """
        super().__init__(*args, **kwargs)
        print("below super() in form---------***********-----------------**************------------")

        placeholders = {
            # 'm_id': 'Message ID',  # needs to add to model
            # 'default_contact_email': 'E-mail for contact,'
            'm_title': "Message Title",
            'm_body': "Message Body",
            'm_sender_email': 'Email for reply',
            'm_share_email_box': 'Allow service provider to view my email for contact',
            'm_receiver': 'Send to:',  # needs to add to model
            'm_sender': 'From',  # needs to add to model
        }  # default_ makes match the model
        print("below place holders ---------***********-----------------**************------------")
