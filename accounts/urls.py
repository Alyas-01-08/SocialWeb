from django.views.generic import RedirectView
from django.urls import path
from .views import (
    UserDetailView,
    UserFollowView,
)
app_name = "accounts"
urlpatterns = [
    path('<slug:username>/', UserDetailView.as_view(), name="detail"),
    path('<slug:username>/follow/', UserFollowView.as_view(), name="follow"),
]
