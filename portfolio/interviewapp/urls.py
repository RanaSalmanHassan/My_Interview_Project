from django.urls import path
from . import views
app_name = 'intapp'
urlpatterns = [
    path('', views.Choose_Month, name='choose_month'),
    path('createint',views.createinterview,name='createint'),
    path('inthome/<int:month>', views.IntDesciption, name='inthome'),
    path('export_to_excel',views.export_to_excel,name='export_to_excel'),
    
]
