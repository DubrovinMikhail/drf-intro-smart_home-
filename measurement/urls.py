from django.urls import path
from measurement.views import GetCreateSensor, UpdateGetSensor, CreateMeasurement

urlpatterns = [
    path('sensors/', GetCreateSensor.as_view()),
    path('sensors/<pk>/', UpdateGetSensor.as_view()),
    path('measurements/', CreateMeasurement.as_view()),
]
