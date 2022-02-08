def employee_query(args):
    query = "INSERT INTO employee(first_name, last_name, PESEL, date_employed, salary, city, street, postal_code, country, house_number) VALUES ('{first_name}','{last_name}','{PESEL}',DATE '{date_employed}',{salary},'{city}','{street}','{postal_code}','{country}',{house_number})"
    query = query.format(first_name = args['first_name'], last_name = args['last_name'], PESEL = args['pesel'], date_employed = args['date_employed'], salary = args['salary'], city = args['city'], street = args['street'], postal_code = args['postal_code'], country = args['country'], house_number = args['house_number'])
    return query
def attendance_query(args):
    query = "INSERT INTO attendance VALUES('{id_employee}',DATE '{attendance_date}',{time_at_work})"
    query = query.format(id_employee = args['id_employee'], attendance_date = args['attendance_date'], time_at_work = args['time_at_work'])
    return query
def contractor_query(args):
    query = "INSERT INTO contractor(name_company, nip, email, city, street, postal_code, country, house_number) VALUES ('{name_company}','{nip}','{email}','{city}','{street}','{postal_code}','{country}','{house_number}')"
    query = query.format(name_company = args['name_company'], nip = args['nip'], email = args['email'], city = args['city'], street = args['street'], postal_code = args['postal_code'], country = args['country'], house_number = args['house_number'])
    return query
def supplier_query(args):
    query = "INSERT INTO supplier(name_company, nip, email, city, street, postal_code, country, house_number) VALUES ('{name_company}','{nip}','{email}','{city}','{street}','{postal_code}','{country}','{house_number}')"
    query = query.format(name_company = args['name_company'], nip = args['nip'], email = args['email'], city = args['city'], street = args['street'], postal_code = args['postal_code'], country = args['country'], house_number = args['house_number'])
    return query
def model_query(args):
    query = "INSERT INTO model(name_material,name_model,price_base,price_promotional,sku,available,description) VALUES ('{name_material}','{name_model}','{price_base}','{price_promotional}','{sku}','{available}','{description}')"
    query = query.format(name_material = args['name_material'], name_model = args['name_model'], price_base = args['price_base'], price_promotional = args['price_promotional'], sku = args['sku'], available = args['available'], description = args['description'])
    return query
def material_query(args):
    query = "INSERT INTO material VALUES ('{name_material}','{color}')"
    query = query.format(name_material = args['name_material'], color = args['color'])
    return query
def delivery_query(args):
    query = "INSERT INTO delivery(date_delivery,id_employee,id_supplier) VALUES (DATE '{date_delivery}','{id_employee}','{id_supplier}')"
    query = query.format(date_delivery = args['date_delivery'], id_employee = args['id_employee'], id_supplier = args['id_supplier'])
    return query
def order_component_query(args):
    query = "INSERT INTO order_component(quantity,id_order,id_model) VALUES ({quantity},{id_order},{id_model})"
    query = query.format(quantity = args['quantity'], id_order = args['id_order'], id_model = args['id_model'])
    return query
def stock_query(args):
    query = "INSERT INTO stock(quantity,id_delivery,name_material) VALUES ({quantity},{id_delivery},'{name_material}')"
    query = query.format(quantity = args['quantity'], id_delivery = args['id_delivery'], name_material = args['name_material'])
    return query
def orders_query(args):
    if('date_finished' not in args or args['date_finished'] == None):
        query = "INSERT INTO orders(date_order,price,id_contractor) VALUES (DATE '{date_order}',{price},{id_contractor})"
        query = query.format(date_order= args['date_order'], price = args['price'], id_contractor = args['id_contractor'])
    else:
        query = "INSERT INTO orders(date_order,price,id_contractor,date_finished) VALUES (DATE '{date_order}',{price},{id_contractor},DATE '{date_finished}')"
        query = query.format(date_order= args['date_order'], price = args['price'], id_contractor = args['id_contractor'], date_finished = args['date_finished'])
    return query

