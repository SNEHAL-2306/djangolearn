from django.urls import path
from . views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView


urlpatterns = [
    # path('',HomeView.as_view(),name='home'),
    path('',PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/',PostCreateView.as_view(),name='post_create'),
    path('post/<int:pk>/edit/',PostUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    

]