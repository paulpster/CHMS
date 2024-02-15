
USE chms;
DROP PROCEDURE IF EXISTS chms.old_customer_booking;

DELIMITER ;;

CREATE PROCEDURE `old_customer_booking`(IN _cid int, IN _vid int, IN _hire timestamp, IN _ret timestamp, _price DECIMAL(10,2) )
BEGIN
    DECLARE _bid int;

    -- TODO: if _hire is more than 7 days int the future. throw an error
    IF DATEDIFF(NOW(), _hire) > 7 THEN
        SIGNAL SQLSTATE '02500'
            SET MESSAGE_TEXT = 'Hire date too far in the future.';
    END IF;

    INSERT INTO chms.booking (customer_id, vehicle_id, date_out, date_in)
    VALUES (_cid, _vid, _hire, _ret);

    -- create a new invoice?
    SELECT LAST_INSERT_ID() INTO _bid;

    -- as requirements for this become more complex, break this out into its own proc
    INSERT INTO chms.invoice (booking_id, invoice_amount)
    VALUES (_bid, _price);

    -- the day of? create payment
    IF DATEDIFF(NOW(), _hire) = 0 THEN
        -- as requirements for this become more complex, break this out into its own proc
        INSERT INTO chms.payment (booking_id, payment_amount, payment_details)
        VALUES (_bid, _price, "Payment Details");
    END IF;

    -- TODO: if _hire is in the future, create a letter?
    IF DATEDIFF(NOW(), _hire) > 0 THEN
        -- as requirements for this become more complex, break this out into its own proc
        INSERT INTO chms.letter (booking_id, letter_content)
        VALUES (_bid, 'Letter Content');
    END IF;

END ;;

DELIMITER ;
