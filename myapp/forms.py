from django import forms
from django.db.models import fields

from myapp.models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['tenant', 'name', 'address', 'tel', 'email']
        labels = {
            'tenant': 'テナント',
            'name': '名前',
            'address': '住所',
            'tel': '電話番号',
            'email': 'e-mail'
        }
