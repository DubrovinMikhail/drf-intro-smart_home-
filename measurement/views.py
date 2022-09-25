# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer


class GetCreateSensor(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class UpdateGetSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class CreateMeasurement(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer