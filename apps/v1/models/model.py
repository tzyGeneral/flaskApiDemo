# encoding: utf-8
from apps import db


class User(db.Document):
    """用户信息"""
    phone = db.IntField(default=0)
    token = db.StringField(required=True, max_length=33)
    uuid = db.StringField(required=True, max_length=33)
    name = db.StringField(required=True, max_length=33)
    pic = db.StringField(required=True, max_length=33)
    createTime = db.DateTimeField()
    meta = {
        "collection": "user_info",
    }