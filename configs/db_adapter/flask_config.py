import os


class Config(object):
    CURRENT_PATH = os.getcwd()
    SECRET_KEY = 'random-key'


class DevelopmentConfig(Config):
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
        },
        'loggers': {
            'werkzeug': {
                'level': 'DEBUG',
                'handlers': ['console', 'flask_file'],
                'propagate': False
            },
            'gunicorn.error': {
                'level': 'ERROR',
                'handlers': ['console', 'flask_file'],
                'propagate': False
            }
        },

    }


