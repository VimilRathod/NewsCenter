from django import forms

#Defining class for the form and defining form elements in it

class SettingsForm(forms.Form):
    TOI = forms.BooleanField(label='TOI', required=False)
    HT = forms.BooleanField(label='HT', required=False)
    CBC = forms.BooleanField(label='CBC', required=False)