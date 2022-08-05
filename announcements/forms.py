from django import forms
from.models import *


class annform(forms.ModelForm):
    class Meta:
        model = announcement
        fields = ('announcement','posted_by','title','course')