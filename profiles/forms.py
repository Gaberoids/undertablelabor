from django import forms
from .models import UserProfile


class UserMyProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # exclude user because not necessary
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_aka': 'AKA',
            # 'default_contact_email': 'E-mail for contact,'
            'default_service_profider': "Service Provider",
            'default_town_or_city': 'Town or City',
            'default_county': 'County',
            'default_postcode': 'Postal Code',   

        }  # default_ makes match the model

#  I think, below is making css changes on the form
        # self.fields['default_aka'].widget.attrs['autofocus'] = True
        # for field in self.fields:
        #     if field != 'default_country':
        #         if self.fields[field].required:
        #             placeholder = f'{placeholders[field]} *'
        #         else:
        #             placeholder = placeholders[field]
        #         self.fields[field].widget.attrs['placeholder'] = placeholder
        #     self.fields[field].widget.attrs['class'] = ('border-black '
        #                                                 'rounded-0 '
        #                                                 'profile-form-input')
        #     self.fields[field].label = False
