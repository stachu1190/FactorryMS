from flask_restful import reqparse
def employee_parser():
    parser = reqparse.RequestParser()
    parser.add_argument("first_name", type=str, help="First name of the employee", required=True)
    parser.add_argument("last_name", type=str, help="Last name of the employee", required=True)
    parser.add_argument("PESEL", type=str, help="Numer PESEL pracownika", required=True)
    parser.add_argument("date_employed", type=str, help="Date in format YYYY-MM-DD", required=True)
    parser.add_argument("salary", type=float, help="Employee salary as float", required=True)
    parser.add_argument("city", type=str, help="City name", required=True)
    parser.add_argument("street", type=str, help="Street name", required=True)
    parser.add_argument("postal_code", type=str, help="City postal code", required=True)
    parser.add_argument("country", type=str, help="Country name", required=True)
    parser.add_argument("house_number", type=int, help="House number", required=True)
    return parser




