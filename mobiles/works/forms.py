from django import forms
from works.models import Mobile
class Mform(forms.ModelForm):
    class Meta:
        model=Mobile
        fields='__all__'
