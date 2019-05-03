from django.forms import ModelForm
from .models import realUrl


class realUrlForm(ModelForm):
    class Meta:
        model   = realUrl
        fields  = ['url']