from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    emp_id = forms.CharField(label='Employee Id',
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control'
                                })
                            )
    name = forms.CharField(label='Name',
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control'
                                })
                            )
    assignment_assign = forms.CharField(label='Assignment Assign',
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control'
                                })
                            )

    start_date = forms.CharField(label='Start Date',
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control'
                                })
                            )
    end_date = forms.CharField(label='End Date',
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control'
                                })
                            )
    class Meta:
        model = Employee
        fields = ['emp_id', 'name', 'assignment_assign', 'start_date', 'end_date']