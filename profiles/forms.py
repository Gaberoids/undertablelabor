from django import forms
from .models import UserProfile


class UserMyProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # exclude user because not necessary
        exclude = ('user',)
