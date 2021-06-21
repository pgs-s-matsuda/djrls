from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from myapp.models import Customer, Tenant
from myapp.forms import CustomerForm

class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'myapp/index.html'

class CustomerIndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'customer/index.html'
    context_object_name = 'customer_list'

    def get_queryset(self):
        return Customer.objects.filter()[:]

class CustomerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customer/detail.html"
    success_url = "/"

class CustomerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customer/detail.html"
    success_url = "/"

class App1IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'app1/index.html'

class App2IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'app2/index.html'