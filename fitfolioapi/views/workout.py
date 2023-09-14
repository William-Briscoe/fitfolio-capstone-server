from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from fitfolioapi.models import Workout

class WorkoutView(ViewSet):
    """functions for the workout table"""

    def list(self, request, pk):
        """handle GET requests for all workouts"""

        query = request.query_params.get('user')