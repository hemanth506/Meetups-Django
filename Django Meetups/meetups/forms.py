from django import forms

from . import models

# it return error when an email it is registered for one meetup 
#       but returns error when it is entered to another one
"""
class RegistrationForm(forms.ModelForm):

    # it is a default python feature
    class Meta:
        model = models.Participant
        fields = ['email']
"""

# the error is rectified in this
class RegistrationForm(forms.Form):
    email = forms.EmailField()

