from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('add_course', views.create_course),
    path('courses/destroy/<int:course_id>', views.remove_course),
    path('delete/<int:course_id>', views.delete_course)
]