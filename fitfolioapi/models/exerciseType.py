from django.db import models

class ExerciseType(models.Model):
    label = models.CharField(max_length=50)