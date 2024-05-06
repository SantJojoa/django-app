from django import forms 
from academics.models import users

class UserForm(forms.ModelForm):
    class Meta:
        Model = users
        field = [
            'email',
            'password',
            'status'
        ]