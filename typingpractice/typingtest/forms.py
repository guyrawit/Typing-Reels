from django import forms
from django.utils.translation import gettext_lazy as _

class TypingForm(forms.Form):
    response = forms.CharField(
        label=_('What did the character say?'),
        widget=forms.TextInput(attrs={'placeholder': 'Start typing here...'})
    )