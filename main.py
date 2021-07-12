from flask import Flask
from flask_restful import Resource, Api, reqparse
import json
import csv

app = Flask(__name__)
api = Api(app)


class Questions2(Resource):
    def get(self):
        data = {}
        with open('input.csv', 'r', encoding="utf8") as inp:
            data2 = csv.DictReader(inp)
            id = 0
            for rows in data2:
                data[id] = rows
                id += 1
        with open('out1.json', 'w', encoding="utf8") as json_file:
            json_file.write(json.dumps(data))
        return data, 200


api.add_resource(Questions2, '/questions')

if __name__ == '__main__':
    app.run(debug=True)  # run our Flask app
