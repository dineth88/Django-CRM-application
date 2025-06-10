import django_filters
from django_filters import DateFilter, CharFilter
from django import forms # Import forms

from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(
        field_name="date_created",
        lookup_expr='gte',
        # Add widget with class 'datepicker'
        widget=forms.DateInput(attrs={'class': 'form-control datepicker', 'placeholder': 'YYYY-MM-DD'})
    )
    end_date = DateFilter(
        field_name="date_created",
        lookup_expr='lte',
        # Add widget with class 'datepicker'
        widget=forms.DateInput(attrs={'class': 'form-control datepicker', 'placeholder': 'YYYY-MM-DD'})
    )
    note = CharFilter(
        field_name="note",
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by note'})
    )

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']