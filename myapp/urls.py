from django.urls import path

from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<uuid:pk>/', views.CustomerUpdateView.as_view(), name='update'),
    path('create/', views.CustomerCreateView.as_view(), name='create'),
]
