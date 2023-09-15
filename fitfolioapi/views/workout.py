from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from fitfolioapi.models import Workout, Exercise

class WorkoutView(ViewSet):
    """functions for the workout table"""
    def retrieve(self, request, pk):
        """Handle GET requests for single workout

        Returns:
            Response -- JSON serialized workout
        """

        workout = Workout.objects.get(pk=pk)
        serializer = WorkoutSerializer(workout)
        return Response(serializer.data)



    def list(self, request):
        """handle GET requests for all workouts"""

        #set a query of user, if there is one, to filter workouts by user pks
        query = request.query_params.get('user')

        #checks if there is a query to filter, if so we filter by user_id, if not we get all objects
        if query:
            Workouts = Workout.objects.filter(user_id=query)
        else:
            Workouts = Workout.objects.all()
            
        serializer = WorkoutSerializer(Workouts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def create(self, request):
        """Handle POST operations for creating a new workout"""

        # Retrieve the user making the request
        user = request.user
        exercise = Exercise.objects.get(pk=request.data["exercise"])

        workout = Workout.objects.create(
            date =request.data['date'],
            reps_distance = request.data['reps_distance'],
            sets_time = request.data['sets_time'],
            weight= request.data['weight'],
            exercise = exercise,
            user=user
        )

        # Deserialize the request data using the WorkoutSerializer
        serializer = WorkoutSerializer(workout)
        return Response(serializer.data)
    

    def update(self, request, pk):
        """Handle PUT requests for updating existing workouts"""

        workout = Workout.objects.get(pk=pk)
        workout.date = request.data['date']
        workout.reps_distance= request.data['reps_distance']
        workout.sets_time = request.data['sets_time']
        workout.weight = request.data['weight']
        workout.exercise = Exercise.objects.get(pk=request.data['exercise'])
        workout.user = request.auth.user

        workout.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    

    def destroy(self, request, pk=None):
        """Handles DELETE requests for workouts"""

        workout = Workout.objects.get(pk=pk)
        workout.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ExerciseSerializer(serializers.ModelSerializer):
    """JSON serializer for workouts"""

    class Meta:
        model = Exercise
        fields = ('id', 'label')


class WorkoutSerializer(serializers.ModelSerializer):
    """JSON serializer for workouts"""

    exercise = ExerciseSerializer(many=False)
    
    class Meta:
        model = Workout
        fields = ('id', 'date', 'reps_distance', 'sets_time', 'weight', 'exercise', 'user')