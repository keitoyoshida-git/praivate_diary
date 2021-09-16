from config.settings import MEDIA_ROOT, MEDIA_URL
from django.urls import path
from django.urls.conf import include
from .import views

# from django.contrib import admin
# from django.contrib.staticfiles.urls import static
# from django.urls import path,include

# from .import settings_common,settings_dev

from django.urls import path

from .import views

app_name = 'diary' 
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('diary-list',views.DiaryListView.as_view(), name="diary_list"),
    path('diary-detail/<int:pk>/',views.DiaryDetailView.as_view(), name="diary_detail"),
    path('diary-create/', views.DiaryCreateView.as_view(), name="diary_create"),
    path('diary-update/<int:pk>/',views.DiaryUpdateView.as_view(), name="diary_update"),
    path('diary-delete/<int:pk>/', views.DiaryDeleteView.as_view(), name="diary_delete"),
]