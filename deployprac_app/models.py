from django.db import models
import re

class CourseManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if not len(post_data['name']) > 5:
            errors['name'] = "The name of the course must be more than 5 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()


class CourseDescriptionManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if not len(post_data['description']) > 15:
            errors['description'] = "The description must be more than 15 characters"
        return errors

class CourseDescription(models.Model):
    course = models.OneToOneField(Course, on_delete = models.CASCADE, primary_key = True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseDescriptionManager()