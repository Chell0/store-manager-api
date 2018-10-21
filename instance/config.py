class Config:
    """Config class."""
    pass


class Production(Config):
    """Production configuration."""
    DEBUG = False
    TESTING = False


class Development(Config):
    """Development configuration."""
    DEBUG = True
    TESTING = False


class Testing(Config):
    """Testing configuration."""
    DEBUG = True
    TESTING = True


app_settings = {
    'production': Production,
    'development': Development,
    'testing': Testing
}
