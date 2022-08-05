from django import forms
from.models import Doc


class Docform(forms.ModelForm):
    class Meta:
        model = Doc
        fields = ('file','file_name' )