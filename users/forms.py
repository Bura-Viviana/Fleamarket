from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password, password_validators_help_text_html
from producers.models import Producers

AuthUser = get_user_model()


class RegisterForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=30, required=True)
    last_name = forms.CharField(label='Last name', max_length=30, required=True)
    username = forms.CharField(label='Username', max_length=30, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True,
                               help_text=password_validators_help_text_html)
    confirm_password = forms.CharField(label='Confirm password', widget=forms.PasswordInput, required=True)
    email = forms.CharField(label="Email", max_length=50, required=False)
    type = forms.ChoiceField(label='User Type', widget=forms.RadioSelect, choices=(('producer', 'Producer'), ('customer', 'Customer')))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        try:
            AuthUser.objects.get(username=username)
        except AuthUser.DoesNotExist:
            return username
        else:
            raise forms.ValidationError(f'The username {username} already exists.')

    def clean_password(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        username = self.cleaned_data.get('username')

        password = self.cleaned_data.get('password')

        user = AuthUser(
            first_name=first_name,
            last_name=last_name,
            username=username

        )
        validate_password(password, user)
        return password

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if password_confirmation != password:
            raise forms.ValidationError('incorrect password confirmation')
        return password_confirmation

    def clean_email(self):
        email = self.cleaned_data.get('email')
        parts = email.split('@')
        if len(parts) != 2:
            raise forms.ValidationError('Email must be like something@domain.com')
        return email

    def save(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        email = self.cleaned_data.get('email')


        user = AuthUser.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email
        )
        if self.cleaned_data.get('type') == 'producer':
            db_producer = Producers(
                user=user,
                about=f'{first_name} - {last_name}',
                picture='producers/default.jpg'
            )
            db_producer.save()

        return user
