from django.urls import path
from . import views

urlpatterns = [
    #Appointment appointment_list appointment_detail
    path('appointment/', views.appointment_list, name='appointment_list_get'),
    path('appointment/', views.appointment_list, name='appointment_list_post'),
    path('appointment/<int:pk>/', views.appointment_detail, name='appointment_detail_get'),
    path('appointment/<int:pk>/', views.appointment_detail, name='appointment_detail_put'),
    path('appointment/<int:pk>/', views.appointment_detail, name='appointment_detail_delete'),

    #Evaluation Report evaluation_report_list evaluation_report_detail
    path('evaluation/', views.evaluation_report_list, name='evaluation_report_list_get'),
    path('evaluation/', views.evaluation_report_list, name='evaluation_report_list_post'),
    path('evaluation/<int:pk>/', views.evaluation_report_detail, name='evaluation_report_detail_get'),
    path('evaluation/<int:pk>/', views.evaluation_report_detail, name='evaluation_report_detail_put'),
    path('evaluation/<int:pk>/', views.evaluation_report_detail, name='evaluation_report_detail_delete'),

    #Assessment assessment_list assessment_detail
    path('assessment/', views.assessment_list, name='assessment_list_get'),
    path('assessment/', views.assessment_list, name='assessment_list_post'),
    path('assessment/<int:pk>/', views.assessment_detail, name='assessment_detail_get'),
    path('assessment/<int:pk>/', views.assessment_detail, name='assessment_detail_put'),
    path('assessment/<int:pk>/', views.assessment_detail, name='assessment_detail_delete')
]