from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    holes = models.IntegerField(validators=[MinValueValidator(6), MaxValueValidator(36)])
    tee_type = models.CharField(max_length=8)
