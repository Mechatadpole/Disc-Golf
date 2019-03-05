from django.db import models
<<<<<<< HEAD


# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    holes = models.IntegerField(min_val= 6, max_val= 36)
=======
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    holes = models.IntegerField(validators=[MinValueValidator(6), MaxValueValidator(36)])
>>>>>>> 4c8fe140afae3e185bd480cfb644fb7a2ec1bb50
    tee_type = models.CharField(max_length=8)
