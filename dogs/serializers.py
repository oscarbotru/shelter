from rest_framework import serializers

from dogs.models import Dog
from dogs.validators import validator_scam_words


class DogSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[validator_scam_words])

    class Meta:
        model = Dog
        fields = '__all__'
