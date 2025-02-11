from django import forms
from promo.models import CallbackRequest
from restaurant_admin.models import User, RestaurantInfo
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Restaurant Name', min_length=1, max_length=150)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Your password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat your password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("User Already Exist")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError("Email Already Exist")
        return email

    def clean_password1(self):
        username = self.cleaned_data.get('username')
        password1 = self.cleaned_data.get('password1')

        if username and password1 and password1.lower() == username.lower():
            raise ValidationError("The password is too similar to the username.")
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user


class LoginUserForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'forminput'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'forminput'}))


class CallbackRequestForm(forms.ModelForm):
    class Meta:
        model = CallbackRequest
        fields = ['name', 'phone_number', 'email']

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not phone_number.startswith('+995'):
            raise forms.ValidationError("Phone number must start with '+995'.")
        if len(phone_number) != 13:
            raise forms.ValidationError("Phone number must contain exactly 12 digits including the country code.")
        if not phone_number[1:].isdigit():
            raise forms.ValidationError("Phone number must contain only digits after '+'.")
        return phone_number