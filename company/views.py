from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView
# Create your views here.
from .models import Company, Department, Employee
from django import forms


class EditEmployee(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class EditDepartment(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class EditCompany(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'



class CompaniesListView(ListView):
    model = Company
    template_name = 'company/company_list.html'


class EmployeeListView(ListView):
    model = Employee
    template_name = 'company/employee_list.html'


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'company/company_detail.html'


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'company/department_detail.html'


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'company/employee_detail.html'


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'company/employee_update.html'
    form_class = EditEmployee


class CompanyUpdateView(UpdateView):
    model = Company
    template_name = 'company/company_update.html'
    form_class = EditCompany


class DepartmentUpdateView(UpdateView):
    model = Department
    template_name = 'company/department_update.html'
    form_class = EditDepartment
