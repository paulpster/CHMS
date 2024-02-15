
USE chms;
DROP PROCEDURE IF EXISTS chms.new_customer_booking;

DELIMITER ;;

CREATE PROCEDURE `new_customer_booking`(IN _cust_name text, IN _cust_addr text, IN _contact text, 
        IN _vid int, IN _hire timestamp, IN _ret timestamp, _price DECIMAL(10,2))
BEGIN
    DECLARE _cid int;

    INSERT INTO chms.customer (customer_name, customer_address, contact_number) 
    VALUES (_cust_name, _cust_addr, _contact);

    SELECT LAST_INSERT_ID() INTO _cid;

    CALL chms.old_customer_booking(_cid, _vid, _hire, _ret, _price);
END ;;

DELIMITER ;
