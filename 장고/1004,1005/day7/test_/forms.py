
from django import forms
from .models import Test

class TestFrom(forms.ModelForm):

    class Meta:
        model = Test
        fields = ['title', 'content']