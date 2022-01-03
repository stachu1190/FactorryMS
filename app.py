from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import psycopg2
from psycopg2 import Error
import signal
import parsers
import sys
import queries

def shutdown(signal_received, frame):
    cursor.close()
    connection.close()
    print("REST api has been shut down")
    exit(0)

signal.signal(signal.SIGTERM, shutdown)
signal.signal(signal.SIGINT, shutdown)

app = Flask(__name__)
#app.secret_key = "siemaeniuwpuscmnie"
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

def print_psycopg2_exception(err):
    err_type, err_obj, traceback = sys.exc_info()
    line_num = traceback.tb_lineno
    print ("\npsycopg2 ERROR:", err, "on line number:", line_num)
    print ("psycopg2 traceback:", traceback, "-- type:", err_type)
    print ("\nextensions.Diagnostics:", err.diag)
    print ("pgerror:", err.pgerror)
    print ("pgcode:", err.pgcode, "\n")
    return err.pgcode, err.pgerror

class Employee(Resource):
    def post(self):
        parser = parsers.employee_parser()
        args = parser.parse_args()
        query = queries.employee_query(args)
        cursor.execute(query)
        connection.commit()
        return {}, 201
class Attendance(Resource):
    def post(self):
        parser = parsers.attendance_parser()
        args = parser.parse_args()
        query = queries.attendance_query(args)
        cursor.execute("SELECT id_employee FROM employee WHERE id_employee = {id_employee}".format(id_employee = args['id_employee']))
        if(cursor.fetchall() == []):
            return {'error' : 'There is no employee with given id'},404
        else:
            try:
                cursor.execute(query)
                connection.commit()
            except Exception as err:
                code, error = print_psycopg2_exception(err)
                connection.rollback()
                if(code == "23505"):
                    return {"error" : "Unique Violation - given record already exists"}, 409
                else:
                    return {"error" : error, "code" : code}, 400
            return {}, 201
class Contractor(Resource):
    def post(self):
        parser = parsers.contractor_parser()
        args = parser.parse_args()
        query = queries.contractor_query(args)
        cursor.execute(query)
        connection.commit()
        return {}, 201
        

api.add_resource(Employee, "/employee")
api.add_resource(Attendance, "/attendance")

if __name__ == "__main__":
	app.run(debug=True)