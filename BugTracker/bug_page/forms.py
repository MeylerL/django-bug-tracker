from django import forms
from django.contrib.auth.models import User
from .models import TrackerUser, BugDetail


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','email','password']

class UserFormExtraInfo(forms.ModelForm):
    class Meta:
        model = TrackerUser
        fields = ['role']


class BugForm(forms.ModelForm):
    assigned_to = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
    class Meta:
        model = BugDetail
        exclude = ["created_at", "updated_at"]
