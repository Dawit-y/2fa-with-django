from django import forms
from .models import Code

class CodeForm(forms.ModelForm):
    number = forms.CharField(label="Code" ,  help_text="Enter your code from SMS")
    class Meta:
        model = Code
        fields = ('number',)
