from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password, password_validators_help_text_html

AuthUser = get_user_model()


class RegisterForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=30, required=True)
    last_name = forms.CharField(label='Last name', max_length=30, required=True)
    username = forms.CharField(label='Username', max_length=30, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True,
                               help_text=password_validators_help_text_html)
    confirm_password = forms.CharField(label='Confirm password', widget=forms.PasswordInput, required=True)

    def clean_username(self):
        username=self.cleaned_data.get('username')

        try:
            AuthUser.objects.get(username= username)
        except AuthUser.DoesNotExist:
            return username
        else:
            raise forms.ValidationError('The username is already exist.')

    def clean_password(self):
        first_name=self.cleaned_data.get('first_name')
        last_name=self.cleaned_data.get('last_name')
        username=self.cleaned_data.ger('username')

        password = self.cleand_data.get('password')

        user=AuthUser(
            first_name=first_name,
            last_name=last_name,
            username=username

        )
        validate_password(password, user)
        return password
    def clean_password_confirmation(self):
        password=self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if password_confirmation != password:
            raise forms.ValidationError('incorrect password confirmation')
        return password_confirmation

    def save(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        username = self.cleaned_data.ger('username')

        password = self.cleand_data.get('password')

        user = AuthUser.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password
        )
        return user




