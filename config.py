from re import DEBUG

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'secret key qwerty 123'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://mydb:qwerty123@db/my_db'


class MyConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:rootpassword@localhost/sys'


class TestConfig(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:rootpassword@localhost/test_db'
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    WTF_CSRF_ENABLED = False