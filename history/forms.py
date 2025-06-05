from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Event

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control rounded-pill',
            'placeholder': 'Имя пользователя'
        })
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control rounded-pill',
            'placeholder': 'Ваше имя'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control rounded-pill',
            'placeholder': 'Email'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control rounded-pill',
            'placeholder': 'Пароль'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control rounded-pill',
            'placeholder': 'Повторите пароль'
        })

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return cd['password2']

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control rounded-pill',
            'placeholder': 'Имя пользователя'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control rounded-pill',
            'placeholder': 'Пароль'
        })

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'description', 'image', 'categories', 'tags', 'region']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categories'].widget.attrs.update({
            'class': 'form-select rounded-pill',
        })
        self.fields['tags'].widget.attrs.update({
            'class': 'form-select rounded-pill',
        })
        self.fields['region'].widget.attrs.update({
            'class': 'form-control rounded-pill',
            'placeholder': 'Регион',
        })
