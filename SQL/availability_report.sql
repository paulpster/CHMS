USE chms;

 DROP PROCEDURE IF EXISTS chms.availability_report;

DELIMITER ;;

CREATE PROCEDURE `availability_report`(IN _report_date date)
BEGIN
    SELECT v.vehicle_id, v.vin, v.vehicle_name, v.vehicle_type 
    FROM chms.vehicle v INNER JOIN chms.booking b ON (v.vehicle_id = b.vehicle_id AND b.date_out < _report_date AND b.date_in > _report_date)
    WHERE b.vehicle_id IS NULL ORDER BY v.vehicle_name;
END;;
DELIMITER ;
