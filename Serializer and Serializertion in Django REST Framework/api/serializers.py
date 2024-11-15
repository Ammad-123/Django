from rest_framework import serializers
# from .models import Student

class StudentSerializer(serializers.Serializer):
    fname = serializers.CharField(max_length=100)
    lname = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
 

