CREATE DATABASE chms;
-- default DB enginge should be fine (at least to get started)

/* just a few of may fields that could be here */
CREATE TABLE chms.customer (
    customer_id int NOT NULL AUTO_INCREMENT,
    customer_name text NOT NULL,
    customer_address text,
    contact_number  text,
    create_date timestamp DEFAULT NOW(),
    PRIMARY KEY (customer_id)
);
-- to assist in look ups (when we have lots of customers)
CREATE INDEX customer_customer_name ON chms.customer (customer_name(25));
ALTER TABLE chms.customer AUTO_INCREMENT = 1000;

-- I do not love all these similar names, worry about confusing tables and columns
CREATE TABLE chms.vehicle_type (
    vehicle_type varchar(15),
    capacity int,
    PRIMARY KEY (vehicle_type)
);
-- zero passengers meaning: I do not know how many passengers.
INSERT INTO chms.vehicle_type VALUES ('Small Car', 4), ('Family Car', 7), ('Van', 0);

CREATE TABLE chms.vehicle (
    vehicle_id  int NOT NULL AUTO_INCREMENT,
    vin text,
    vehicle_name text NOT NULL,
    vehicle_type varchar(15),
    create_date timestamp DEFAULT NOW(),
    PRIMARY KEY (vehicle_id),
    FOREIGN KEY (vehicle_type) REFERENCES chms.vehicle_type (vehicle_type)
);
CREATE INDEX vehicle_vehicle_name ON chms.vehicle (vehicle_name(25));
ALTER TABLE chms.vehicle AUTO_INCREMENT = 1000;

/* the customer_id foreign key should not be there for this exercise, but should be there in real life */
/* customer_id foreign key will be OK if there are no bookings to disrupt things */
CREATE TABLE chms.booking (
    booking_id int NOT NULL AUTO_INCREMENT,
    customer_id int NOT NULL,
    vehicle_id int NOT NULL,
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
ALTER TABLE chms.booking AUTO_INCREMENT = 1000;

/*
    An invoice is to be auto generated upon 'booking'. That probably mean upon the insert or a booking record.
    A trigger can be used to do this, but that is meaningless with out some thing on the front end to notice.
    A stored proc that puts away the booking can to this as well.
*/

-- Not entirely sure about these and what they need to hold based on the requirements
-- I do know that I should record that these things were done (recd payment, create invoice, sent letter).
CREATE TABLE chms.payment (
    booking_id  int NOT NULL,
    payment_amount  DECIMAL(10, 2),
    payment_details  text,
    create_date timestamp DEFAULT NOW(),
    PRIMARY KEY (booking_id),
    FOREIGN KEY (booking_id) REFERENCES chms.booking (booking_id)
);

CREATE TABLE chms.invoice (
    invoice_id  int NOT NULL AUTO_INCREMENT,
    booking_id  int NOT NULL,
    invoice_amount DECIMAL(10, 2),
    create_date timestamp DEFAULT NOW(),
    PRIMARY KEY (invoice_id),
    FOREIGN KEY (booking_id) REFERENCES chms.booking (booking_id)
);
ALTER TABLE chms.invoice AUTO_INCREMENT = 1000;

CREATE TABLE chms.letter (
    booking_id  int NOT NULL,
    letter_content text,
    create_date timestamp DEFAULT NOW(),
    PRIMARY KEY (booking_id),
    FOREIGN KEY (booking_id) REFERENCES chms.booking (booking_id)
);
