from django import forms
from .models import Update, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddUpdateForm(forms.ModelForm):
    body = forms.CharField(max_length=200, required=True, widget=forms.widgets.Textarea(attrs={"placeholder": "Enter your Nexus update!", "class": "form-control"}),
    label="")

    class Meta:
        model = Update
        exclude = ("user", "likes",)

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'placeholder': 'Enter your email address...', 'class': 'form-control'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your first name....', 'class': 'form-control'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your last name...', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username....'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter your password....'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Enter your password again to confirm....'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

class ProfilePicForm(forms.ModelForm):
    profile_image = forms.ImageField(label='Profile Picture')

    class Meta:
        model = Profile
        fields = ('profile_image',)
