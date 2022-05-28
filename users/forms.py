from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Profile

# here we are inheriting the user creation form that comes with Django, but we are adding the email field so 
# we can validate a user using their email
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserProfileForm(forms.ModelForm):
    periods = [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (6,6),
        (7,7),
    ]
    period = forms.ChoiceField(choices=periods)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model = Profile
        fields = ['first_name','last_name','period']


# this will create a form that will allow a user to update their profile information
# a model form creates a form that is able to interact with a specific model
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email']


'''
# this will create a form that will alow a user update their profile picture
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
'''