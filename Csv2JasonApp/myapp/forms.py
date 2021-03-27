from django import forms
class SearchForm(forms.Form):
    category=forms.CharField(label="Enter Category")
    age=forms.CharField(label="Enter Minimum Age",required=False)
    name=forms.CharField(label="Enter Name",required=False)