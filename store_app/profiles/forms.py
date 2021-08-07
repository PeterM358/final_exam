from django import forms

from store_app.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('url', 'user', )
