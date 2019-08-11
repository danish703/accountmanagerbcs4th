from django import forms
from django.forms import ModelForm
from .models import Expenses,Category

class ExpensesForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'title'}))
    description =forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    bill = forms.FileField(widget=forms.FileInput())
    rupes = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model= Expenses
        fields = ['title','description','bill','rupes','category']