from redis import StrictRedis
import logging

class Config():
    SECRET_KEY = '12356'

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql://root:123@127.0.0.1:3306/new_information'
    SQLALCHEMY_TRACK_MODIFICATIONS  = False

    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = '6379'

    # 配置flask_session, 把session存入redis数据库
    SESSION_TYPE = 'redis'
    SESSION_USE_SIGNER = True  # 加密session
    SESSION_REDIS = StrictRedis(host=REDIS_HOST,port=REDIS_PORT)  # 告诉session redis数据库的位置
    PERMNAENT_SESSION_LIFETIME = 60*60*24  # 一天


class DevelopmentConfig(Config):
    LEVEL_LOG = logging.DEBUG

class UnittestConfig(Config):
    TESTTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123@127.0.0.1:3306/new_information_test'
    LEVEL_LOG = logging.DEBUG

class ProductConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123@127.0.0.1:3306/new_information_info'
    LEVEL_LOG = logging.ERROR


configs = {
    'dev':DevelopmentConfig,
    'pro':ProductConfig,
    'Unit':UnittestConfig
}