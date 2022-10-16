from django.urls import path

from app.views import CurrentWeatherView, HistoryWeatherView

urlpatterns = [
    path('weather/', CurrentWeatherView.as_view(), name='weather'),
    path('history/', HistoryWeatherView.as_view(), name='history')
]
