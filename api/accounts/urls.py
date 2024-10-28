from django.urls import path
from . import views

urlpatterns = [
    path('users/' , views.UserPostListCreate.as_view() , name = 'user-view-create'),
    path('users/<int:pk>/' , views.UserPostRetrieveUpdateDestroy.as_view() , name = 'update'),
]
