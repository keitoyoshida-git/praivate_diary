from config.settings import MEDIA_ROOT, MEDIA_URL
from django.urls import path
from django.urls.conf import include
from .import views

# from django.contrib import admin
# from django.contrib.staticfiles.urls import static
# from django.urls import path,include

# from .import settings_common,settings_dev

app_name = 'diary' 
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    # path('accounts/',include('allauth.urls')),
]

# urlpatterns += static(settings_common.MEDIA_URL,
# document_root=settings_dev.MEDIA_ROOT)