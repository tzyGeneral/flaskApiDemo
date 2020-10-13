# encoding: utf-8
from flask import Blueprint
from flask_restful import Api


def register_views(app):
    from .views import baseView
    api = Api(app)
    api.add_resource(baseView.HelloWorldView, '/hi')


def create_blueprint_v1():
    """
    注册蓝图->v1版本
    """
    bp_v1 = Blueprint('v1', __name__)
    register_views(bp_v1)
    return bp_v1
