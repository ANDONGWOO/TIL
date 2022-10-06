from django import forms
from .models import Movie

class MovieFrom(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['title', 'summary','running_time']#모델 전체