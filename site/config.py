import os

basedir = os.path.abspath(os.path.dirname(__file__))
app_name = "app"


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ftftfiub958fjg6vrtgitfjkthgfo8w496b6r9r6b76'
    MONGODB_DB = 'aim_high'
    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017

    UPLOAD_FOLDER = os.path.join(basedir, app_name, 'static/')

    @staticmethod
    def init_app(app):
        pass


class DevCongig(Config):
    DEBUG = True


class ProdConfig(Config):
    pass


config = {
    'dev': DevCongig,
    'prod': ProdConfig
}
