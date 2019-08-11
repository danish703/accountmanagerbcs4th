from django import forms
from django.forms import ModelForm
from .models import Income
class IncomeForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'title'}))
    description =forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    rupes = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model= Income
        fields = ['title','description','rupes']