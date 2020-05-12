from django.db import models
from multiselectfield import MultiSelectField
from apps.authentication.models import User


class Activity(models.Model):
    CATEGORY_CHOICES = (
        ('Art', 'Art'),
        ('Educational', 'Educational'),
        ('Science', 'Science'),
        ('Games', 'Games'),
        ('Developmental', 'Developmental'),
    )
    AGE_RANGE_CHOICES = (
        ('Infant', 'Infant'),
        ('Toddler', 'Toddler'),
        ('Kindergarten', 'Kindergarten'),
        ('First-Grade', 'First-Grade'),
        ('Second-Grade', 'Second-Grade'),
        ('Third-Grade', 'Third-Grade'),
        ('Fourth-Grade', 'Fourth-Grade'),
        ('Fifth-Grade', 'Fifth-Grade'),
        ('Sixth-Grade', 'Sixth-Grade'),
    )
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category = MultiSelectField(choices=CATEGORY_CHOICES)
    age_range = MultiSelectField(choices=AGE_RANGE_CHOICES)
    summary = models.CharField(max_length=200)
    supplies = models.CharField(max_length=300)
    body = models.TextField()
    image = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title
