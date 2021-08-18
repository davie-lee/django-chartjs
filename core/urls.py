from django.contrib import admin
from django.urls import path
from dataviz import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='landing'),
    path('bar-chart/', views.bar_chart, name='bar-chart'),
    path('pie-chart/', views.pie_chart, name='pie-chart'),
]