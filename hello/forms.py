from django import forms

class AddPersonForm(forms.Form):
    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)
    year = forms.IntegerField()

class AddProducerForm(forms.Form):
    name = forms.CharField(max_length=64)
    city = forms.CharField(max_length=64)
    year = forms.IntegerField()