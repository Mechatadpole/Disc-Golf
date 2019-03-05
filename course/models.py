from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    holes = models.IntegerField(min_val= 6, max_val= 36)
    tee_type = models.CharField(max_length=8)