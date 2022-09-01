from django.urls import path
from blog import views

urlpatterns = [
    path("",views.index,name="home"),
    path('mert-caliskan-pdf/', views.download_file),
]

