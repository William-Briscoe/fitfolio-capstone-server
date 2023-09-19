from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from fitfolioapi.models import Exercise, ExerciseType

class ExerciseTypeView(ViewSet):

    """functions for the exercise type table"""
    

    def list(self, request):
        """handle GET requests for all exerciseTypes"""

        exerciseType = ExerciseType.objects.all()
            
        serializer = ExerciseTypeSerializer(exerciseType, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




class ExerciseTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for exercises"""
    
    class Meta:
        model = Exercise
        fields = ('id', 'label')
