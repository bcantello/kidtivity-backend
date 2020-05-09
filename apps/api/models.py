from django.db import models
from apps.authentication.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Activity(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100, null=False)
    category = models.ManyToManyField(Category, related_name="categories")
    summary_description = models.CharField(max_length=200, null=False)
    supplies = models.CharField(max_length=500, blank=True)
    instructions = models.CharField(max_length=2000, blank=True)
    # Image upload field goes here

    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"

    def __str__(self):
        return self.name
