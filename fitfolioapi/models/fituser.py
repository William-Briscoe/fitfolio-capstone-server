from django.db import models
from django.contrib.auth.models import User



class FitUser(models.Model):
    """the table for all users"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def full_name(self):
        """combine first and last names into new property"""
        return f'{self.user.first_name} {self.user.last_name}'
