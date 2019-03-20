from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from users.models import Profile

# Different inputs and values for the addCourse prompt

class Course(models.Model):
    course_name = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    holes = models.IntegerField(validators=[MinValueValidator(6), MaxValueValidator(36)])
    tee_type = models.CharField(max_length=8)
    play = models.BooleanField(default=False)

    def __str__(self):
        return self.course_name

class Review(models.Model):
    thoughts = models.CharField(max_length=1800)
    author = models.ForeignKey(Profile, on_delete="CASCADE")
    crse = models.ForeignKey(Course, on_delete="CASCADE")
