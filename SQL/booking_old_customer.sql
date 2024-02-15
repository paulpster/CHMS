
USE chms;
DROP PROCEDURE IF EXISTS chms.old_customer_booking;

DELIMITER ;;

CREATE PROCEDURE `old_customer_booking`(IN _cid int, IN _vid int, IN _hire timestamp, IN _ret timestamp, _price DECIMAL(10,2) )
BEGIN
    DECLARE _bid int;

    -- TODO: if _hire is more than 7 days int he future. throw an error

    INSERT INTO chms.booking (customer_id, vehicle_id, date_out, date_in)
    VALUES (_cid, _vid, _hire, _ret);

    -- TODO: if _hire is in the future, create a letter?

    -- create a new invoice?
    SELECT LAST_INSERT_ID() INTO _bid;


    INSERT INTO chms.invoice (booking_id, invoice_amount)
    VALUES (_bid, _price);
END ;;

DELIMITER ;
