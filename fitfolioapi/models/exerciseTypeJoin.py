from django.db import models

class Exercise_Type_Join(models.Model):
    exercise = models.ForeignKey("Exercise", on_delete=models.CASCADE)
    exercise_type = models.ForeignKey("ExerciseType", on_delete=models.CASCADE)