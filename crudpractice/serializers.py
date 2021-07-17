from rest_framework import serializers
from crudpractice.models import StudentData

class StudentDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StudentData
        fields = (
            'id',
            'name',
            'college',
            'subject'
        )