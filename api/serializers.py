from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()    
    timestamp = serializers.DateTimeField(read_only=True)
