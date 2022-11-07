from rest_framework import serializers

class emailsenderserializer(serializers.Serializer):
    name   = serializers.CharField(max_length = 255)
    email  = serializers.EmailField()
    sender = serializers.CharField(max_length=255)
    body   = serializers.CharField()
    remail = serializers.EmailField()

    class Meta:
        fields = [
            'name',
            'email',
            'sender',
            'body',
            'remail'
        ]