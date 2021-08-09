from django import forms

from store_app.profiles.models import Profile, Cart


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('url', 'user', )


class AddCashForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ('cash', )

