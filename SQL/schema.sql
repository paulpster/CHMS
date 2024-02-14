CREATE DATABASE chms;
-- default DB enginge should be fine (at least to get started)

/* just a few of may fields that could be here */
CREATE TABLE chms.customer (
    customer_id int,
    customer_name text,
    customer_address text,
    contact_number  text,
    create_date timestamp DEFAULT NOW(),
    PRIMARY KEY (customer_id)
);
-- to assist in look ups (when we have lots of customers)
CREATE INDEX customer_customer_name ON chms.customer (customer_name(25));

-- I do not love all these similar names, worry about confusing tables and columns
CREATE TABLE chms.vehicle_type (
    vehicle_type varchar(15),
    capacity int,
    PRIMARY KEY (vehicle_type)
);
-- zero passengers meaning: I do not know how many passengers.
INSERT INTO chms.vehicle_type VALUES ('Small Car', 4), ('Family Car', 7), ('Van', 0);

CREATE TABLE chms.vehicle (
    vehicle_id  int,        
    vin text,
    vehicle_name text,
    vehicle_type varchar(15),
    create_date timestamp DEFAULT NOW(),
    PRIMARY KEY (vehicle_id),
    FOREIGN KEY (vehicle_type) REFERENCES chms.vehicle_type (vehicle_type)
);
CREATE INDEX vehicle_vehicle_name ON chms.vehicle (vehicle_name(25));

CREATE TABLE chms.booking (
    booking_id int,
    customer_id int,
    vehicle_id int,
    date_out    timestamp,       -- date the customer picks up the car
    date_in     timestamp,       -- date the customer returns the car
    create_date timestamp DEFAULT NOW(),
    PRIMARY KEY (booking_id),
    FOREIGN KEY (customer_id) REFERENCES chms.customer (customer_id),
    FOREIGN KEY (vehicle_id) REFERENCES chms.vehicle (vehicle_id),
    CONSTRAINT seven_day_rental CHECK (DATEDIFF(date_in, date_out) < 7),
    CONSTRAINT seven_day_advance CHECK (DATEDIFF(date_out, create_date) < 7)
);
CREATE INDEX booking_date_out ON chms.booking (date_out);

-- Not entirely sure about these and what they need to hold based on the requirements
-- I do know that I should record that these things were done (recd payment, create invoice, sent letter).
CREATE TABLE chms.payment (
    booking_id  int,
    payment_amount  DECIMAL(10, 2),
    payment_details  text,
    create_date timestamp DEFAULT NOW(),
    PRIMARY KEY (booking_id),
    FOREIGN KEY (booking_id) REFERENCES chms.booking (booking_id)
);

CREATE TABLE invoice (
    invoice_id  int,
    booking_id  int,
    invoice_amount DECIMAL(10, 2),
    create_date timestamp DEFAULT NOW(),
    PRIMARY KEY (invoice_id),
    FOREIGN KEY (booking_id) REFERENCES chms.booking (booking_id)
);

CREATE TABLE letter (
    booking_id  int,
    letter_content text,
    create_date timestamp DEFAULT NOW(),
    PRIMARY KEY (booking_id),
    FOREIGN KEY (booking_id) REFERENCES chms.booking (booking_id)
);
