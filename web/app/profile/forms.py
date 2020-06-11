from django import forms
from .models import Profile, ProfileManager
from allauth.account.forms import ChangePasswordForm


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('signature', 'gender', 'phone_number')
        exclude = ('user',)
        # widgets = {'author': forms.ChoiceField(choices=ProfileManager.GENDER_CHOICES)}

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].widget.attrs.update({
            'class': 'form-control',
            'value': "Profile.get_phone_number",
        })
        self.fields['phone_number'].widget.attrs['placeholder'] = '1111111111' or self.fields['phone_number'].label
        self.fields['gender'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['signature'].widget.attrs.update({
            'class': 'form-control',
            'rows': 2,
        })


class ChangePassForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super(ChangePassForm, self).__init__(*args, **kwargs)
        self.fields['oldpassword'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control'
        })


class ImageFileUploadForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)


class SignupForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'gender')

    def signup(self, request, user):
        # Save your user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        # user.profile.nationality = self.cleaned_data['nationality']
        user.profile.gender = self.cleaned_data['gender']
        user.profile.save()
