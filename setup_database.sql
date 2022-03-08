DROP TABLE attendance CASCADE;
DROP TABLE contractor CASCADE;
DROP TABLE delivery CASCADE;
DROP TABLE employee CASCADE;
DROP TABLE material CASCADE;
DROP TABLE model CASCADE;
DROP TABLE order_component CASCADE;
DROP TABLE orders CASCADE;
DROP TABLE stock CASCADE;
DROP TABLE supplier CASCADE;

CREATE TABLE attendance (
    id_employee INTEGER NOT NULL,
    attendance_date               DATE NOT NULL,
    time_at_work         FLOAT NOT NULL
);

ALTER TABLE attendance ADD CONSTRAINT attendance_pk PRIMARY KEY ( id_employee,
                                                                  attendance_date);

CREATE TABLE contractor (
    id_contractor INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY,
    name_company  VARCHAR(100) NOT NULL,
    nip           VARCHAR(20) NOT NULL,
    email         VARCHAR(100) NOT NULL,
    city          VARCHAR(50) NOT NULL,
    street        VARCHAR(50) NOT NULL,
    postal_code   VARCHAR(10) NOT NULL,
    country       VARCHAR(50) NOT NULL,
    house_number  INTEGER NOT NULL
);

ALTER TABLE contractor ADD CONSTRAINT contractor_pk PRIMARY KEY ( id_contractor );

CREATE TABLE delivery (
    id_delivery          INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY,
	date_delivery      DATE NOT NULL,
    id_supplier INTEGER,
    id_employee INTEGER
);

ALTER TABLE delivery ADD CONSTRAINT delivery_pk PRIMARY KEY ( id_delivery );

CREATE TABLE employee (
    id_employee   INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY,
    first_name     VARCHAR(50) NOT NULL,
	last_name     VARCHAR(50) NOT NULL,
    pesel         VARCHAR(11) NOT NULL,
    date_employed DATE NOT NULL,
	salary        FLOAT NOT NULL,
    city          VARCHAR(50) NOT NULL,
    street        VARCHAR(50) NOT NULL,
    postal_code   VARCHAR(10) NOT NULL,
    country       VARCHAR(50) NOT NULL,
    house_number  INTEGER NOT NULL
);

ALTER TABLE employee ADD CONSTRAINT employee_pk PRIMARY KEY ( id_employee );

CREATE TABLE material (
    name_material VARCHAR(50) NOT NULL,
	color 		  VARCHAR(50) NOT NULL
);

ALTER TABLE material ADD CONSTRAINT material_pk PRIMARY KEY ( name_material );

CREATE TABLE model (
    id_model               INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY,
    name_material VARCHAR(50) NOT NULL,
    name_model             VARCHAR(50) NOT NULL,
    price_base             FLOAT NOT NULL,
    price_promotional      FLOAT,
    sku                    VARCHAR(15) NOT NULL,
    available              CHAR(1) NOT NULL,
    description            VARCHAR(200)
);

ALTER TABLE model ADD CONSTRAINT model_pk PRIMARY KEY ( id_model );

CREATE TABLE order_component (
    quantity        INTEGER NOT NULL,
    id_order  		INTEGER NOT NULL,
    id_model  INTEGER NOT NULL
);

ALTER TABLE order_component ADD CONSTRAINT order_component_pk PRIMARY KEY ( id_order,
                                                                            id_model );

CREATE TABLE stock (
    quantity      INTEGER NOT NULL,
    id_delivery   INTEGER NOT NULL,
    name_material VARCHAR(50) NOT NULL
);

ALTER TABLE stock ADD CONSTRAINT stock_pk PRIMARY KEY ( id_delivery,
                                                        name_material );

CREATE TABLE supplier (
    id_supplier  INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY,
    name_company VARCHAR(100) NOT NULL,
    nip          VARCHAR(10) NOT NULL,
    email        VARCHAR(100) NOT NULL,
    city         VARCHAR(50) NOT NULL,
    street       VARCHAR(50) NOT NULL,
    postal_code  VARCHAR(10) NOT NULL,
    country      VARCHAR(50) NOT NULL,
    house_number INTEGER NOT NULL
);

ALTER TABLE supplier ADD CONSTRAINT supplier_pk PRIMARY KEY ( id_supplier );

CREATE TABLE orders (
    id_order                 INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY,
    date_order               DATE NOT NULL,
    price                    FLOAT NOT NULL,
    id_contractor            INTEGER NOT NULL,
    date_finished            DATE
);

ALTER TABLE orders ADD CONSTRAINT orders_pk PRIMARY KEY ( id_order );

ALTER TABLE attendance
    ADD CONSTRAINT attendance_employee_fk FOREIGN KEY ( id_employee )
        REFERENCES employee ( id_employee )
			ON DELETE CASCADE;

ALTER TABLE delivery
    ADD CONSTRAINT delivery_employee_fk FOREIGN KEY ( id_employee )
        REFERENCES employee ( id_employee )
			ON DELETE SET NULL;

ALTER TABLE delivery
    ADD CONSTRAINT delivery_supplier_fk FOREIGN KEY ( id_supplier )
        REFERENCES supplier ( id_supplier )
			ON DELETE SET NULL;

ALTER TABLE model
    ADD CONSTRAINT model_material_fk FOREIGN KEY ( name_material )
        REFERENCES material ( name_material )
			ON DELETE SET NULL;

ALTER TABLE order_component
    ADD CONSTRAINT order_component_model_fk FOREIGN KEY ( id_model )
        REFERENCES model ( id_model )
			ON DELETE CASCADE;

ALTER TABLE order_component
    ADD CONSTRAINT order_component_orders_fk FOREIGN KEY ( id_order )
        REFERENCES orders ( id_order )
			ON DELETE CASCADE;

ALTER TABLE stock
    ADD CONSTRAINT stock_delivery_fk FOREIGN KEY ( id_delivery )
        REFERENCES delivery ( id_delivery )
			ON DELETE CASCADE;

ALTER TABLE stock
    ADD CONSTRAINT stock_material_fk FOREIGN KEY ( name_material )
        REFERENCES material ( name_material )
			ON DELETE CASCADE;
	

ALTER TABLE orders
    ADD CONSTRAINT orders_contractor_fk FOREIGN KEY ( id_contractor )
        REFERENCES contractor ( id_contractor )
            ON DELETE SET NULL;
			
CREATE OR REPLACE FUNCTION monthlySalarySum()
RETURNS FLOAT AS
    $body$
    DECLARE
    BEGIN
        return (select SUM(salary) FROM employee);
    END
    $body$
LANGUAGE plpgsql;	


create or replace procedure giveRaise(
   vpesel VARCHAR(11), 
   vraise int
) 
as $body$
begin
    update employee 
    set salary = salary + vraise
    where pesel = vpesel;
    commit;
end$body$
language plpgsql;


INSERT INTO employee (first_name,last_name, pesel, date_employed, salary, city, street, postal_code, country, house_number)
VALUES ('Jan', 'Kowalski', '12345678901', DATE '2021-12-09', 2137.00, 'Poznań', 'Morawskiego', '12-345', 'Polska', 3);
INSERT INTO employee (first_name,last_name, pesel, date_employed, salary, city, street, postal_code, country, house_number)
VALUES ('Jakub', 'Zmuda', '11111111111', DATE '2021-12-31', 12000.00, 'Zbąszynek', 'Knyszyńska', '69-420', 'Polska', 20);
INSERT INTO employee (first_name,last_name, pesel, date_employed, salary, city, street, postal_code, country, house_number)
VALUES ('Igor', 'Pawłowski', '22222222222', DATE '2021-09-11', 120.00, 'Knyszyn', 'Zbąszynecka', '22-333', 'Polska', 10);


INSERT INTO attendance (id_employee, attendance_date, time_at_work)
VALUES (1, DATE '2021-12-09', 8);
INSERT INTO attendance (id_employee, attendance_date, time_at_work)
VALUES (1, DATE '2021-12-10', 8); 
INSERT INTO attendance (id_employee, attendance_date, time_at_work)
VALUES (1, DATE '2021-12-11', 8.5); 

INSERT INTO contractor (name_company, nip, email, city, street, postal_code, country, house_number)
VALUES ('Śmierciopol', '1234567890', 'smierciopol@gmail.com', 'Poznań', 'Głogowska', '12-345', 'Polska', 142);
INSERT INTO contractor (name_company, nip, email, city, street, postal_code, country, house_number)
VALUES ('Tanatos', '0987654321', 'tanatos@gmail.com', 'Poznań', 'Słowiańska', '12-111', 'Polska', 13);

INSERT INTO supplier (name_company, nip, email, city, street, postal_code, country, house_number)
VALUES ('Drewnopol', '1111111111', 'drewnopol@gmail.com', 'Poznań', 'Naramowicka', '12-333', 'Polska', 14);
INSERT INTO supplier (name_company, nip, email, city, street, postal_code, country, house_number)
VALUES ('Lignum', '2222222222', 'lignum@gmail.com', 'Skwierzyna', 'Konopnickiej', '66-440', 'Polska', 4);

INSERT INTO delivery (date_delivery, id_supplier, id_employee)
VALUES (DATE '2021-12-11', 1, 1);
INSERT INTO delivery (date_delivery, id_supplier, id_employee)
VALUES (DATE '2021-12-11', 2, 1);

INSERT INTO material
VALUES ('Dąb', 'Ciemnobrązowy');
INSERT INTO material
VALUES ('Sosna', 'Jasnobrązowy');

INSERT INTO model (name_material, name_model, price_base, sku, available, description)
VALUES ('Dąb', 'Luksja', 1000.00, '48295029', 'Y', 'Dębowa trumna z białą wyściółką');
INSERT INTO model (name_material, name_model, price_base, sku, available, description)
VALUES ('Sosna', 'Awersja', 1500.00, '1982543', 'N', 'Sosnowa trumna z białą wyściółką oraz czerwonymi akcentami');

INSERT INTO orders (date_order, price, id_contractor, date_finished)
VALUES (DATE '2021-12-05', 3000, 1, DATE '2021-12-08');
INSERT INTO orders (date_order, price, id_contractor)
VALUES (DATE '2021-12-11', 3000, 2);

INSERT INTO order_component
VALUES (3, 2, 1);
INSERT INTO order_component
VALUES (2, 1, 2);

INSERT INTO stock
VALUES (10, 1, 'Dąb');
INSERT INTO stock
VALUES (5, 1, 'Sosna');
INSERT INTO stock
VALUES (15, 2, 'Sosna');



