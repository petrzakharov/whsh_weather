from datetime import datetime, timedelta

from conf.settings import APIKEY, OPENWEATHER_RESOURCE, UNITS
from django.db import connection
from django.db.models import Max, Min
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MowscowWeather
from .utils import OpenWeather


class CurrentWeatherView(APIView):
    def get(self, request, *args, **kwargs):
        start_dt = datetime.now()
        end_dt = start_dt - timedelta(minutes=60)
        current_temp = MowscowWeather.objects.filter(
            datetime__lte=start_dt,
            datetime__gte=end_dt
        ).values('temperature').order_by('-datetime').first()
        if not current_temp:
            current_temp = OpenWeather().update_weather(
                OPENWEATHER_RESOURCE,
                UNITS,
                APIKEY
            )
        return JsonResponse(current_temp, safe=True, status=status.HTTP_200_OK)


class HistoryWeatherView(APIView):
    def get(self, request, *args, **kwargs):
        period = MowscowWeather.objects.aggregate(start_period=Min('date'), end_period=Max('date'))
        if not any(period.values()):
            return Response(status=status.HTTP_404_NOT_FOUND)
        cursor = connection.cursor()
        cursor.execute(
            """
                WITH RECURSIVE dates(date) AS (
                  VALUES(%s)
                  UNION ALL
                  SELECT date(date, '+1 day')
                  FROM dates
                  WHERE date < %s
                )
                SELECT
                    t1.date, (CASE WHEN avg_temp IS NULL THEN 0 ELSE avg_temp END) as temperature
                FROM
                    dates t1 LEFT JOIN (
                    SELECT date, AVG(temperature) as avg_temp FROM weather GROUP BY date
                    ) t2
                ON t1.date = t2.date
            """, [*period.values()]
        )
        result = [{element[0]: {'temperature': element[1]}} for element in cursor.fetchall()]
        return JsonResponse(result, safe=False, status=status.HTTP_200_OK)
