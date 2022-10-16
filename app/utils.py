import logging

import requests
from conf.settings import (API_ERROR, CITY, CONNECTION_ERROR, OUT_API_ERROR,
                           SUCCESS_REQUEST)
from rest_framework import status
from rest_framework.exceptions import APIException

from .models import MowscowWeather

logger = logging.getLogger()

logging.basicConfig(
    filename=__name__ + '.log',
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


class OpenWeather:
    @staticmethod
    def _save_to_db(temperature: float) -> dict:
        MowscowWeather.objects.create(temperature=temperature)
        return {
            'temperature': temperature
        }

    @staticmethod
    def _make_request(url: str, units: str, apikey: str) -> float:
        params = {
            'q': CITY,
            'units': units,
            'appid': apikey
        }
        params_request = dict(
            url=url,
            params=params
        )
        try:
            response = requests.get(**params_request)
            params.pop('appid')
        except requests.exceptions.RequestException as exception:
            logger.error(
                CONNECTION_ERROR.format(response.status, response.reason, params_request, exception)
            )
            raise APIException(code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=OUT_API_ERROR)
        data = response.json()
        if status_code := data.get('cod') != 200:
            logger.error(API_ERROR.format(status_code, data.get('message'), params_request))
            raise APIException(code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=OUT_API_ERROR)
        logger.info(SUCCESS_REQUEST)
        return data['main']['temp']

    def update_weather(self, url: str, units: str, apikey: str) -> dict:
        temperature = self._make_request(url, units, apikey)
        return self._save_to_db(temperature)
