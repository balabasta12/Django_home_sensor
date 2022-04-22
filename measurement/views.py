# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from django.shortcuts import render

from .models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorDetailSerializer, SensorChangeSerializer


@api_view(['GET', 'POST'])
def measurement(request):
    measurement_ = Measurement.objects.all()
    ser = MeasurementSerializer(measurement_, many=True)
    return Response(ser.data)


@api_view(['GET', 'POST'])
def sensor(request):
    sensor_ = Sensor.objects.all()
    ser = SensorDetailSerializer(sensor_, many=True)
    return Response(ser.data)


class SensorChangeView(UpdateAPIView):  # Обновить информацию по конкретному датчику
    queryset = Sensor.objects.all()
    serializer_class = SensorChangeSerializer

class SensorView(RetrieveAPIView):  # Получить информацию по конкретному датчику
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer