from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile, Vocabulary


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['lesson_price']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['lesson_price'].widget.attrs.update({'class': 'form-control'})


class VocabularyForm(forms.ModelForm):
    class Meta:
        model = Vocabulary
        fields = ['phrase', 'translate', 'examples', 'comments']
        widgets = {
            'phrase': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phrase'}),
            'translate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter translation (optional)'}),
            'examples': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter examples (optional)'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter comments (optional)'}),
        }
