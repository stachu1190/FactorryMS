def employee_query(args):
    query = "INSERT INTO employee(first_name, last_name, PESEL, date_employed, salary, city, street, postal_code, country, house_number) VALUES ('{first_name}','{last_name}','{PESEL}',DATE '{date_employed}',{salary},'{city}','{street}','{postal_code}','{country}',{house_number})"
    query = query.format(first_name = args['first_name'], last_name = args['last_name'], PESEL = args['PESEL'], date_employed = args['date_employed'], salary = args['salary'], city = args['city'], street = args['street'], postal_code = args['postal_code'], country = args['country'], house_number = args['house_number'])
    return query
def attendance_query(args):
    query = "INSERT INTO attendance VALUES('{id_employee}',DATE '{attendance_date}',INTERVAL '{time_at_work} hours')"
    query = query.format(id_employee = args['id_employee'], attendance_date = args['attendance_date'], time_at_work = args['time_at_work'])
    return query