from django.urls import path

from dogs.apps import DogsConfig
from dogs.views import DogListAPIView, DogCreateAPIView

app_name = DogsConfig.name

urlpatterns = [
    # path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('dogs/', DogListAPIView.as_view(), name='list'),
    path('dogs/create/', DogCreateAPIView.as_view(), name='dog_create'),
    # path('dogs/upadte/<int:pk>/', DogUpdateAPIView.as_view(), name='dog_update'),
    # path('dogs/delete/<int:pk>/', DogDeleteAPIView.as_view(), name='dog_delete'),
]
