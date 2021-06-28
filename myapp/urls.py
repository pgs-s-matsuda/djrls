from django.urls import path

from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('customer/', views.CustomerIndexView.as_view(), name='customerindex'),
    path('customer/<uuid:pk>/', views.CustomerUpdateView.as_view(),
         name='customerupdate'),
    path('customer/create/', views.CustomerCreateView.as_view(),
         name='customercreate'),
    path('app1/', views.App1IndexView.as_view(), name='app1index'),
    path('app2/', views.App2IndexView.as_view(), name='app2index'),
]
