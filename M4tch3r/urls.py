from django.contrib import admin
from django.urls import path
from canmatch import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('CandidateFinder/<search>/', views.CandidateFinder, name='matchme'),
]
