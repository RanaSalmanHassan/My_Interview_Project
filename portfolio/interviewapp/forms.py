from django import forms
from .models import Interview


class Create_Interview_Form(forms.ModelForm):
  
    class Meta:
        model = Interview
        exclude = ('user',)
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
