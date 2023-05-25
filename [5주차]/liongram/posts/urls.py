from django.urls import path
from .views import post_list_view, post_create_view, post_udpate_view, post_detail_view, post_delete_view

# 세션
from .views import post_create_form_view

app_name = 'posts'

urlpatterns = [
    path('', post_list_view, name='post-list'),
    # path('create/', post_create_view, name='post-create'),
    # 세션
    path('create/', post_create_form_view, name='post-create'),
    path('<int:id>/', post_detail_view, name='post-detail'),
    path('<int:id>/edit/', post_udpate_view, name='post-update'),
    path('<int:id>/delete/', post_delete_view, name='post-delete'),
]
