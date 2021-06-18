from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from myapp.models import Customer
from myapp.forms import CustomerForm

# Create your views here.
class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'myapp/index.html'
    context_object_name = 'customer_list'

    def get_queryset(self):
        return Customer.objects.filter()[:]

class CustomerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "myapp/detail.html"
    success_url = "/"

class CustomerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "myapp/detail.html"
    success_url = "/"

