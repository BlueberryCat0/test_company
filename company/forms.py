from django import forms
from .models import Employee

class EditEmployee(forms.ModelForm):
    class Meta:
        model = Employee
