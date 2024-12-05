from django.urls import path
from . import views

urlpatterns = [
    path('course/', views.course_list, name='course_list_get'),
    path('course/', views.course_list, name='course_list_post'),
    path('course/<int:pk>/', views.course_detail, name='course_detail_get'),
    path('course/<int:pk>/', views.course_detail, name='course_detail_put'),
    path('course/<int:pk>/', views.course_detail, name='course_detail_delete'),
]