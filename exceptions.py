class ServerErrorException(Exception):
    """Для ошибок при обращении по http к Open-Weather"""
    pass

class DataBaseException(Exception):
    """Для ошибок при запросе к БД"""
    pass