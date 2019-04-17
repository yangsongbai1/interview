from flask import Flask, request
from flask_restful import Resource, Api

import datetime

app = Flask(__name__)
api = Api(app)


class Add(Resource):
    def post(self):
        value_array = request.json.get('value_array', [])
        if value_array and isinstance(value_array, list):
            result = 0
            for item in value_array:
                result += item.get('value', 0)
            return {"result": result}
        else:
            return {"result": "请求参数有错误"}


class GetDate(Resource):
    def get(self):
        now = datetime.datetime.now()
        date = now.strftime('%Y-%m-%d')
        return {"date": date}


class Chat(Resource):
    def post(self):
        msg = request.form.get('msg', '')
        if '您好' in msg and '再见' in msg:
            result = '天气不错。'
        elif '您好' in msg:
            result = '您好，您吃了吗？'
        elif '再见' in msg:
            result = '回见了您内。'
        else:
            result = ''
        return {'result': result}


api.add_resource(Add, '/add')
api.add_resource(GetDate, '/get_date')
api.add_resource(Chat, '/chat')

if __name__ == '__main__':
    app.run()
