
from django import forms

class ZWForm(forms.Form):
    t_url = forms.CharField(max_length=254,
                           widget=forms.TextInput({
                               'name': 'form-url',
                               'class': 'form-url w3-input w3-border w3-animate-input',
                               'style': 'width:60%'}))



class ZWMP4toMP3Form(forms.Form):
    c_url = forms.FileField(max_length= None,allow_empty_file = False)