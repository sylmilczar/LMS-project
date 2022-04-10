from django.urls import path

from . import views

app_name = 'courses'

urlpatterns = [
    path('create', views.CreateCourseView.as_view(), name='create-course'),
]
