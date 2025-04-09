"""
Модуль для получения координат города по его имени из базы данных `russian_cities.db`

"""

import sqlite3

from typing import Optional
from loguru import logger

from models import Coordinates
from exceptions import DataBaseException

logger.add('app.log',  format="{time} {level} {message}", level="INFO")

DB_FILE_NAME = 'russian_cities.db'

def get_city_coordinates(city_name: str) -> Optional[Coordinates]:
    """
    Возвращает координаты объект Coordinates или None 
    
    """
    try:
        coordinates = None
        with sqlite3.connect(DB_FILE_NAME) as con:
            cursor = con.cursor()
            cursor.execute("""
                SELECT lat, lon FROM cities 
                WHERE name = ?
            """, (city_name.title(),))

            result = cursor.fetchone()
            if result:
                coordinates = Coordinates(result[0], result[1])
    except DataBaseException:
        logger.error(f'Ошибка БД при работе с городом {city_name}')
    finally:
        return coordinates

