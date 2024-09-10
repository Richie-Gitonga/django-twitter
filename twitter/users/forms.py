from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'location', 'bio', 'profilepicture')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('bio', 'location', 'profilepicture')


# class DocUserCreationForm(UserCreationForm):
#     class Meta:
#         model = DocCustomUser
#         fields = ('username', 'email', 'location', 'bio', 'profilepicture')

