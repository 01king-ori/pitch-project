import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
    SECRET_KEY=os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST='app/static/photos'
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")
    SIMPLEMDE_JS_IIFE=True
    SIMPLEMDE_USE_CDN=True

class ProdConfig(Config):
    
    DEBUG=False
    

class TestConfig(Config):
        SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://vincent:xpsviewer*@localhost/pitcher_test'

class DevConfig(Config):
         SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://vincent:xpsviewer*@localhost/pitcher-app'
        DEBUG=True

config_options = {
 'development':DevConfig,
 'production':ProdConfig,
 'test':TestConfig
}           
