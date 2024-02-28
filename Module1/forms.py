from django import forms
class IntergerDateForm(forms.Form):
    integer_value= forms.IntegerField()
    date_value= forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))