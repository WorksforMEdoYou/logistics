from django.urls import path
from . import views

urlpatterns = [
    path('subscribers/', views.subscriber_list, name='subscriber_list_get'),
    path('subscribers/', views.subscriber_list, name='subscriber_list_post'),
    path('subscribers/<int:pk>/', views.subscriber_detail, name='subscriber_detail_get'),
    path('subscribers/<int:pk>/', views.subscriber_detail, name='subscriber_detail_put'),
    path('subscribers/<int:pk>/', views.subscriber_detail, name='subscriber_detail_delete'),
]