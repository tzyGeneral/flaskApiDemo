# encoding: utf-8
from apps.v1 import create_blueprint_v1
from flask import Flask
from flask_caching import Cache
from flask_mongoengine import MongoEngine
from celery import Celery
from config import Conf
import logging
import os
from logging.handlers import TimedRotatingFileHandler


def register_blueprints(app):
    # 注册版本
    app.register_blueprint(create_blueprint_v1(), url_prefix='/api/v1')


memCache = Cache(config={'CACHE_TYPE': 'memcached'})
db = MongoEngine()


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


def create_app():
    if not os.path.exists('logs'): os.mkdir('logs')
    handler = TimedRotatingFileHandler('logs/flask.log', encoding='UTF-8')
    logging_format = logging.Formatter(
        '[%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - line:%(lineno)s]: %(message)s')
    handler.setFormatter(logging_format)
    app = Flask(__name__)
    app.config.from_object(Conf)
    app.secret_key = app.config['SECRET_KEY']
    db.init_app(app)
    memCache.init_app(app)
    setattr(app, 'memCache', memCache)
    app.logger.addHandler(handler)
    register_blueprints(app)
    return app


app = create_app()
celery = make_celery(app)
