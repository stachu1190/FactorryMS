from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import psycopg2
from psycopg2 import Error

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
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


if __name__ == "__main__":
	app.run(debug=True)