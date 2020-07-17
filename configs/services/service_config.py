import os


class Config(object):
    CURRENT_PATH = os.getcwd()
    SECRET_KEY = 'random-key'


class ProductionConfig(Config):
    #
    # Salt-api server configuration
    #
    SALT_API_IP = 'saltstack'
    SALT_API_PORT = '8000'
    SALT_API_ADDRESS = SALT_API_IP + ':' + SALT_API_PORT
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
    # Path to file of addresses
    #
    ADDRESS_FILE = 'configs/addresses.xlsx'

    #
    # DBAdapter
    #

    # DBAdapter URL
    DBADAPTER_URL = 'http://db_adapter:5050/api'

    #
    # DBSender
    #

    # DBsender as Process
    DBSENDER_IS_PROCESS = False

    # Default False
    MULTITHREADING = False

    #
    # Message queue
    #
    MQ_HOST = 'mq'
    MQ_PORT = 5672

    #
    # Refresh timer
    #

    # Timer for getting grains.
    # Default 300
    GRAINS_TIMER = 300

    # Timer for getting status of hosts.
    # Default 30
    PING_TIMER = 30

    # Timer for getting version of hosts.
    # Default 30
    VERSION_TIMER = 30

    # Timer for collecting statistics.
    # Default 60
    STATISTIC_TIMER = 60

    # Timer for getting keys.
    # Default 300
    KEY_TIMER = 300

    #
    # TaskScheduler
    #

    # Timer for getting tasks.
    # Default 60
    SHEDULER_TIMER = 60

    #
    # Filters
    #

    # Time of action expired
    # Default 10 min
    MINUTES_OF_EXPIRED = 10

    #
    # Test TKControl client
    #
    TEST_USER = 'admin'

    #
    # Salt nodegroup patterns
    #
    NODEGROUP_PATTERNS = {
        'medpc-img': {
            'regex': 'medpc-.*',
            'grain': {
                'osfullname': 'ALT',
                'cpuarch': 'x86_64',
            }
        },
        'linux': {
            'grain': {
                'kernel': 'Linux'
            }
        }
    }

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
            'service_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'level': 'DEBUG',
                'formatter': 'default',
                'filename': './logs/debug.log',
                'maxBytes': 1024*1024*10,  # 10 mb
            },
            'sender_logging': {
                'class': 'logging.handlers.RotatingFileHandler',
                'level': 'DEBUG',
                'formatter': 'default',
                'filename': './logs/sender_debug.log',
                'maxBytes': 1024*1024*10,  # 10 mb
            },
        },
        'loggers': {
            'werkzeug': {
                'level': 'DEBUG',
                'handlers': ['console', 'service_file'],
                'propagate': False
            },
            'db_adapter': {
                'level': 'DEBUG',
                'handlers': ['sender_logging'],
                'propagate': False
            }
        },
    }


class DevelopmentConfig(ProductionConfig):
    DBADAPTER_URL = 'http://localhost:5050/api'
    MQ_HOST = 'localhost'
