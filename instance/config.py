class Config:
    pass


class Production(Config):
    DEBUG = False
    TESTING = False


class Development(Config):
    DEBUG = True
    TESTING = False


class Testing(Config):
    DEBUG = True
    TESTING = True


app_settings = {
    'production': Production,
    'development': Development,
    'testing': Testing
}
