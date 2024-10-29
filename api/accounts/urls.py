from django.urls import path
from .views import UserPostRetrieveUpdateDestroy , UserPostListCreate , UserPostList


urlpatterns = [
    path('users/' , UserPostListCreate.as_view() , name = 'userpostlistcreate'),
    path('users/<int:pk>/', UserPostRetrieveUpdateDestroy.as_view(), name='userpostdetail'),
    path('user-post-list/' , UserPostList.as_view() , name = 'userpostlist'),
]
