"""
Загружает токен Телеграм-бота, токен для Open-Weather и базовый URL для обращения
в переменные API_TOKEN_TG, API_TOKEN_WEATHER, URL_API

"""
import os

from dotenv import load_dotenv


load_dotenv()
API_TOKEN_TG = os.getenv('TG_TOKEN')
API_TOKEN_WEATHER = os.getenv('OPEN_WEATHER_TOKEN')
URL_API = os.getenv('URL_API')