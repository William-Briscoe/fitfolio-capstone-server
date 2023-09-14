from django.db import models

class Exercise(models.Model):
    label = models.CharField(max_length=50)
    exercise_types = models.ManyToManyField("ExerciseType", through='Exercise_Type_Join', related_name='exercise_types')