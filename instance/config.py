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
    DATABASE_URI = 'postgresql://localhost/test_db' 


class Production(Config):
    """Production configuration."""
    DEBUG = False
    TESTING = False


app_settings = {
    'production': Production,
    'development': Development,
    'testing': Testing
}
