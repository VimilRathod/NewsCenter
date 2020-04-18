from django import forms

class SettingsForm(forms.Form):
    TOI = forms.BooleanField(label='TOI', required=False)
    HT = forms.BooleanField(label='HT', required=False)
    CBC = forms.BooleanField(label='CBC', required=False)