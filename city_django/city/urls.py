from django.urls import path
from city import views

app_name = 'city'
urlpatterns = [
    path('DaData/', views.dadata_geocoding, name='DaData')
]
