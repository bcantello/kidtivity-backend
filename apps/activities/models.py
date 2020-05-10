from django.db import models
from apps.authentication.models import User


class Activity(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category = models.CharField(max_length=20, choices=[
        ('Art', 'Art'),
        ('Educational', 'Educational'),
        ('Science', 'Science'),
        ('Games', 'Games'),
        ('Developmental', 'Developmental'),
    ])
    age_range = models.CharField(max_length=20, choices=[
        ('Infant', 'Infant'),
        ('Toddler', 'Toddler'),
        ('Kindergarten', 'Kindergarten'),
        ('First-Grade', 'First-Grade'),
        ('Second-Grade', 'Second-Grade'),
        ('Third-Grade', 'Third-Grade'),
        ('Fourth-Grade', 'Fourth-Grade'),
        ('Fifth-Grade', 'Fifth-Grade'),
        ('Sixth-Grade', 'Sixth-Grade'),
        ('Middle-School', 'Middle-School'),
        ('High-School', 'High-School'),
    ])
    summary = models.CharField(max_length=200)
    supplies = models.CharField(max_length=300)
    body = models.TextField()
    # image = models.ImageField(upload_to='activity_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title
