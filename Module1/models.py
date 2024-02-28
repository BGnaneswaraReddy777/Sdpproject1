from django.db import models

# Create your models here.
class Gnani(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    class Meta:
        db_table="Gnani"

class Feedback(models.Model):
    Firstname=models.TextField(max_length=200)
    Lastname=models.TextField(max_length=200)
    Email=models.EmailField(primary_key=True)
    Comments=models.TextField(max_length=200)
    class Meta:
        db_table = "Feedback"




from django import forms
class PieChartForm(forms.Form):
    y_values = forms.CharField(label='Y Values', help_text='Enter comma-separated values')
    labels = forms.CharField(label='Labels', help_text='Enter comma-separated labels')
