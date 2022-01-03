from flask_restful import reqparse

def employee_parser():
    parser = reqparse.RequestParser()
    parser.add_argument("first_name", type=str, help="First name of the employee", required=True)
    parser.add_argument("last_name", type=str, help="Last name of the employee", required=True)
    parser.add_argument("PESEL", type=str, help="Employee PESEL", required=True)
    parser.add_argument("date_employed", type=str, help="Date in format YYYY-MM-DD", required=True)
    parser.add_argument("salary", type=float, help="Employee salary as float", required=True)
    parser.add_argument("city", type=str, help="City name", required=True)
    parser.add_argument("street", type=str, help="Street name", required=True)
    parser.add_argument("postal_code", type=str, help="City postal code", required=True)
    parser.add_argument("country", type=str, help="Country name", required=True)
    parser.add_argument("house_number", type=int, help="House number", required=True)
    return parser
def attendance_parser():
    parser = reqparse.RequestParser()
    parser.add_argument("id_employee", type=int, help="ID of the employee", required=True)
    parser.add_argument("attendance_date", type=str, help="Date in format YYYY-MM-DD", required=True)
    parser.add_argument("time_at_work", type=int, help="hours in work passed as an integer", required=True)
    return parser
def contractor_parser():
    parser = reqparse.RequestParser()
    parser.add_argument("name_company", type=str, help="Name of the company", required=True)
    parser.add_argument("nip", type=str, help="NIP of the company", required=True)
    parser.add_argument("email", type=str, help="Company's email address", required=True)
    parser.add_argument("city", type=str, help="City name", required=True)
    parser.add_argument("street", type=str, help="Street name", required=True)
    parser.add_argument("postal_code", type=str, help="City postal code", required=True)
    parser.add_argument("country", type=str, help="Country name", required=True)
    parser.add_argument("house_number", type=int, help="House number", required=True)
    return parser
def supplier_parser():
    parser = reqparse.RequestParser()
    parser.add_argument("name_company", type=str, help="Name of the company", required=True)
    parser.add_argument("nip", type=str, help="NIP of the company", required=True)
    parser.add_argument("email", type=str, help="Company's email address", required=True)
    parser.add_argument("city", type=str, help="City name", required=True)
    parser.add_argument("street", type=str, help="Street name", required=True)
    parser.add_argument("postal_code", type=str, help="City postal code", required=True)
    parser.add_argument("country", type=str, help="Country name", required=True)
    parser.add_argument("house_number", type=int, help="House number", required=True)
    return parser
def orders_parser():
    parser = reqparse.RequestParser()
    parser.add_argument("date_order", type=str, help="Date in format YYYY-MM-DD", required=True)
    parser.add_argument("price", type=float, help="Price of the whole order", required=True)
    parser.add_argument("id_contractor", type=int, help="ID of the contractor who ordered", required=True)
    parser.add_argument("date_finished", type=str, help="Date in format YYYY-MM-DD", required=False)
    return parser
def delivery_parser():
    parser = reqparse.RequestParser()
    parser.add_argument("delivery_date", type=str, help="Date in format YYYY-MM-DD", required=True)
    parser.add_argument("id_suppier", type=int, help="ID of the supplier who delivered ordered supplies", required=True)
    parser.add_argument("id_employee", type=int, help="ID of the employee who took the delivery", required=True)
    return parser
def material_parser():
    parser = reqparse.RequestParser()
    parser.add_argument("name_material", type=str, help="Name of the material", required=True)
    parser.add_argument("color", type=str, help="Color of the material", required=False)
    return parser
def model_parser():
    parser = reqparse.RequestParser()
    parser.add_argument("name_material", type=str, help="Name of the material", required=True)
    parser.add_argument("name_model", type=str, help="Name of the model", required=True)
    parser.add_argument("price_base", type=float, help="Base price of the product of this model", required=True)
    parser.add_argument("price_promotional", type=float, help="Price of the product of this model on sale", required=False)
    parser.add_argument("sku", type=str, help="SKU number of the model", required=True)
    parser.add_argument("available", type=str, help="Y if the product of this model is available, N if not", required=True)
    parser.add_argument("description", type=str, help="Description of the model", required=False)
    return parse
def order_component_parser():
    parser.add_argument("quantity", type=int, help="Quantity of the ordered product", required=True)
    parser.add_argument("id_order", type=int, help="ID of the order which consists of given component", required=True)
    parser.add_argument("id_model", type=int, help="ID of the model which given component represents", required=True)
    return parser
def stock_parser():
    parser.add_argument("quantity", type=int, help="Quantity of material delivered in given delivery", required=True)
    parser.add_argument("name_material", type=str, help="Name of the material", required=True)
    parser.add_argument("id_delivery", type=int, help="ID of the delivery in which the stock was registered", required=True)
    return parser









