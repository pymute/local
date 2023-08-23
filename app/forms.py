from django import forms
from .models import News

class NewsForms(forms.ModelForm):
    title_uz = forms.CharField()
    title_ru = forms.CharField(required=False)
    title_en = forms.CharField(required=False)

    text_uz = forms.CharField()
    text_ru = forms.CharField(required=False)
    text_en = forms.CharField(required=False)

class Meta:
    model = News
    exclude = ['title','text']
