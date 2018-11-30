from django.urls import path
from .views import (CompaniesListView, CompanyDetailView, DepartmentDetailView, EmployeeDetailView,
    DepartmentUpdateView, CompanyUpdateView, EmployeeUpdateView, EmployeeListView,
    )

app_name='main'

urlpatterns = [
    path('companies/', CompaniesListView.as_view(), name='companies'),
    path('employees/', EmployeeListView.as_view(), name='employees'),

    path('company/<int:pk>/', CompanyDetailView.as_view(), name='company'),
    path('department/<int:pk>/', DepartmentDetailView.as_view(), name='department'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee'),

    path('company/edit/<int:pk>', CompanyUpdateView.as_view(), name='update-company'),
    path('employee/edit/<int:pk>', EmployeeUpdateView.as_view(), name='update-employee'),
    path('department/edit/<int:pk>', DepartmentUpdateView.as_view(), name='update-department'),
]
