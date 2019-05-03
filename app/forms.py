from django.forms import ModelForm,forms
from .models import realUrl


class realUrlForm(ModelForm):
    class Meta:
        model   = realUrl
        fields  = ['url']


    def clean_url(self):
        url = self.cleaned_data.get("url")
        if "http://" in url or "https://" in url:
            return url
        raise forms.ValidationError("Please Enter Valid URL like: http://www.example.com")
