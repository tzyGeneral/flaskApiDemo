from flask_restful import Resource
from flask import request


class HelloWorldView(Resource):
    """测试接口"""

    def __init__(self):
        self.response = "hello world!"

    def get(self):
        rsp = {"code": 1, "msg": "ok"}
        name = request.args.get("name", "")
        try:
            rsp["data"] = self.response + name
        except Exception as e:
            rsp["code"] = -1
            rsp["msg"] = str(e)
        return rsp

    def post(self):
        rsp = {"code": 1, "msg": "ok"}
        name = request.form.get("name", "")
        try:
            rsp["data"] = self.response + name
        except Exception as e:
            rsp["code"] = -1
            rsp["msg"] = str(e)
        return rsp
