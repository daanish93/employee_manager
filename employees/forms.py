
from django import forms 
from .models import Employees, Notes

class EmployeeCreateForm(forms.ModelForm):   
    class Meta():
        fields = ('name', 'location', 'gender', 'birth_date', 'yearly_salary', 'role', 'degree', 'description')
        model = Employees

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['birth_date'].widget.attrs.update({'class': 'datepicker'})

class NoteCreateForm(forms.ModelForm):
    class Meta():
        model = Notes
        fields = ('text',)