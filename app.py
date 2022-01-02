from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import psycopg2
from psycopg2 import Error
import signal
import parsers
import sys
from queries import employee_query

def shutdown(signal_received, frame):
    cursor.close()
    connection.close()
    print("REST api has been shut down")
    exit(0)

signal.signal(signal.SIGTERM, shutdown)
signal.signal(signal.SIGINT, shutdown)

app = Flask(__name__)
api = Api(app)

try:
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="coffin_factory")

    cursor = connection.cursor()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

class Employee(Resource):
    def post(self):
        parser = parsers.employee_parser()
        args = parser.parse_args()
        query = employee_query(args)
        cursor.execute(query)
        connection.commit()
        

api.add_resource(Employee, "/employee")

if __name__ == "__main__":
	app.run(debug=True)