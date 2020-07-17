import os


class Config(object):
    CURRENT_PATH = os.getcwd()
    SECRET_KEY = 'random-key'


class DevelopmentConfig(Config):
    #
    # Salt-api server configuration
    #
    SALT_API_ADDRESS = 'saltstack:8000'
    SALT_API_URL = 'http://' + SALT_API_ADDRESS

    #
    # Salt user configuration
    #
    SALT_API_USERNAME = 'salt'
    SALT_API_PASSWORD = 'saltpass'
    SALT_API_EAUTH = 'sharedsecret'

    #
    # Path to salt-api certificate
    #
    NAME_OF_CRT = 'configs/ca.pem'
    PATH_TO_CRT = Config.CURRENT_PATH + '/' + NAME_OF_CRT

    #
    # Test TKControl client
    #
    TEST_USER = 'admin'

    #
    # Message queue
    #
    MQ_HOST = 'mq'
    MQ_PORT = 5672

    #
    # Logger configuration
    #
    LOGGER_CONFIG = {
        'version': 1,
        'formatters': {'default': {
            'format': '%(asctime)s %(levelname)s: %(message)s',
            'datefmt': '[%m/%d/%Y] %I:%M:%S'
        }},
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'DEBUG',
                'formatter': 'default',
                'stream': 'ext://sys.stdout'
            },
            'flask_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'level': 'DEBUG',
                'formatter': 'default',
                'filename': './logs/debug.log',
                'maxBytes': 1024*1024*10,  # 10 mb
            },
            'web_logger': {
                'class': 'app.logger.web_logger.WebLogger',
                'level': 'DEBUG',
                'formatter': 'default',
                'username': TEST_USER
            }
        },
        'loggers': {
            'werkzeug': {
                'level': 'DEBUG',
                'handlers': ['console', 'flask_file', 'web_logger'],
                'propagate': False
            },
            'gunicorn.error': {
                'level': 'ERROR',
                'handlers': ['console', 'flask_file', 'web_logger'],
                'propagate': False
            }
        },

    }


