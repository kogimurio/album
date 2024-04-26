from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth import get_user_model
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox, ReCaptchaV2Invisible, ReCaptchaV3

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text="Enter a valid Email", required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        User = get_user_model()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use. Please use a different email.")
        return email
    
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control custom-input', 'placeholder': 'First Name'}),
        label='First Name')
    
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control custom-input', 'placeholder': 'Last Name'}),
        label='Last Name')
    
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control custom-input', 'placeholder': 'Email'}),
        label='Email')
    
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control custom-input', 'placeholder': 'Username'}),
        label='Username')
    
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control custom-input', 'placeholder': 'Password'}))
    
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control custom-input', 'placeholder': 'Password Again'}))

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class userLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(userLoginForm, self).__init__(*args, **kwargs)
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Username or Email'}),
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Password'}),
    )
    
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'description', 'image', 'username']

    first_name = forms.CharField(widget=forms.TextInput(
            attrs={'class': 'form-control custom-input', 'placeholder': 'First Name'}),
            label='First Name')

    last_name = forms.CharField(widget=forms.TextInput(
            attrs={'class': 'form-control custom-input', 'placeholder': 'Last Name'}),
            label='Last Name')
        
    email = forms.CharField(widget=forms.EmailInput(
            attrs={'class': 'form-control custom-input', 'placeholder': 'Email'}),
            label='Email')
        
    username = forms.CharField(widget=forms.TextInput(
            attrs={'class': 'form-control custom-input', 'placeholder': 'Username'}),
            label='Username')
    
    description = forms.CharField(widget=forms.TextInput(
            attrs={'class': 'form-control custom-input', 'placeholder': 'Description'}),
            label='Description')


class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']

    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control custom-input', 'placeholder': 'Password'}))
    
    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control custom-input', 'placeholder': 'Password Again'}))
    

class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
    
    email = forms.CharField(widget=forms.EmailInput(
            attrs={'class': 'form-control custom-input', 'placeholder': 'Email'}))
    
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

