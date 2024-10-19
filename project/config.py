import os

class MainConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    IMAGE_UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media', 'bookImages')
    DEBUG = True
    TEST = False


class MysqlConfig:
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'test1'
    MYSQL_PASSWORD = 'password'
    MYSQL_DATABASE = 'exam'
