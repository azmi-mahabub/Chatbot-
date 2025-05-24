from django import forms

class QueryForm(forms.Form):
    query = forms.CharField(label='Describe the part you need', max_length=500)
