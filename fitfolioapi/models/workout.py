from django.db import models

class Workout(models.Model):
    date = models.DateField(auto_now_add=True)
    exercise = models.ForeignKey("Exercise", on_delete=models.CASCADE)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    reps_distance = models.IntegerField()
    sets_time = models.IntegerField()
    weight = models.IntegerField(blank=True, null=True)