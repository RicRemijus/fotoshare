from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    pic = forms.FileField(widget = forms.TextInput(attrs={
        "name":"images",
        "type":"File",
        "class":"form-control",
        "multiple":"True",
    }), label="")

    class Meta:
        model = Image
        fields = ['pic'] 