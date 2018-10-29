import os


class Config:
    """Config class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    DATABASE_URI = os.getenv('DATABASE_URL')


class Development(Config):
    """Development configuration."""
    DEBUG = True
    TESTING = False


class Testing(Config):
    """Testing configuration with a test database."""
    TESTING = True
    DEBUG = True
    DATABASE_URI = os.getenv('DATABASE_URL_TEST')


class Production(Config):
    """Production configuration."""
    DEBUG = False
    TESTING = False


app_settings = {
    'development': Development,
    'testing': Testing,
    'production': Production
}
