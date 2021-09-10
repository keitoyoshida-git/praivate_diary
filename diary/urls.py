from django.urls import path
from django.urls.conf import include
from .import views

app_name = 'diary' 
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('accounts/',include('allauth.urls')),
]
