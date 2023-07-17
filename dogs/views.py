from rest_framework.generics import ListAPIView, CreateAPIView

from dogs.models import Dog
from dogs.paginators import DogPaginator
from dogs.serializers import DogSerializer


class DogListAPIView(ListAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
    pagination_class = DogPaginator


class DogCreateAPIView(CreateAPIView):
    serializer_class = DogSerializer
