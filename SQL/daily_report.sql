
USE chms;
DROP PROCEDURE IF EXISTS chms.daily_report;

DELIMITER ;;

CREATE PROCEDURE `daily_report`(IN _report_date date)
BEGIN
    SELECT c.customer_name, v.vehicle_name, b.date_out, b.date_in 
        FROM chms.booking b INNER JOIN chms.customer c ON b.customer_id = c.customer_id
            INNER JOIN chms.vehicle v ON b.vehicle_id = v.vehicle_id
        WHERE b.date_out < _report_date AND b.date_in > _report_date ORDER BY b.date_out, c.customer_name, v.vehicle_name;
END ;;

DELIMITER ;


