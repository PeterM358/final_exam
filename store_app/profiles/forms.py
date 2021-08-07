from django import forms
from django.db.models import PositiveIntegerField

from store_app.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('url', 'user', )


class AddCashForm(forms.Form):
    amount = forms.IntegerField(
        required=False,
        label='Cash amount',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Add money here'
            }
        )
    )
