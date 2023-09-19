from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from fitfolioapi.models import Exercise, ExerciseType

class ExerciseView(ViewSet):

    """functions for the exercise table"""
    def retrieve(self, request, pk):
        """Handle GET requests for single exercise

        Returns:
            Response -- JSON serialized exercise
        """

        exercise = Exercise.objects.get(pk=pk)
        serializer = ExerciseSerializer(exercise)
        return Response(serializer.data)
    

    def list(self, request):
        """handle GET requests for all exercises"""

        exercise = Exercise.objects.all()
            
        serializer = ExerciseSerializer(exercise, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def create(self, request):
        """Handle POST operations for creating a new exercise"""

        exercise = Exercise.objects.create(
            label = request.data['label']
        )

        # Deserialize the request data using the exerciseSerializer
        serializer = ExerciseSerializer(exercise)

        # Check if exercise_types data is provided in the request
        exercise_type_ids = request.data.get('exercise_types')

        if exercise_type_ids:
            # Use the set() method to assign exercise types to the Exercise instance
            exercise.exercise_types.set(exercise_type_ids)

        return Response(serializer.data)
    

    def update(self, request, pk):
        """Handle PUT requests for updating existing exercises"""

        exercise = Exercise.objects.get(pk=pk)
        exercise.label = request.data['label']

        exercise.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    

    def destroy(self, request, pk=None):
        """Handles DELETE requests for exercises"""

        exercise = Exercise.objects.get(pk=pk)
        exercise.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)




class ExerciseSerializer(serializers.ModelSerializer):
    """JSON serializer for exercises"""
    
    class Meta:
        model = Exercise
        fields = ('id', 'label', 'exercise_types')
        depth=1
