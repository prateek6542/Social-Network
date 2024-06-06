from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserSearchView, FriendRequestViewSet, FriendsListView, PendingFriendRequestsView, UserListView

router = DefaultRouter()
router.register(r'friend-requests', FriendRequestViewSet, basename='friend-request')

urlpatterns = [
    path('search/', UserSearchView.as_view(), name='user-search'),
    path('friends/', FriendsListView.as_view(), name='friends-list'),
    path('pending-requests/', PendingFriendRequestsView.as_view(), name='pending-requests'),
    path('friend-requests/<int:pk>/accept/', FriendRequestViewSet.as_view({'post': 'accept'}), name='friend-request-accept'),
    path('friend-requests/<int:pk>/reject/', FriendRequestViewSet.as_view({'post': 'reject'}), name='friend-request-reject'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('', include(router.urls)),
]
