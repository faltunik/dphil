from django.db import models
from django.conf import settings

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='course/thumbnail/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='courses', blank=True)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='teaching_courses', on_delete=models.CASCADE)

    class meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


