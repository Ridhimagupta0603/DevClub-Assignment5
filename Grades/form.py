from django.forms import ModelForm
from .models import *

class addgradesform(ModelForm):
    class Meta:
        model=grade
        fields="__all__"