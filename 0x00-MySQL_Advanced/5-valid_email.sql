-- trigger that resets valid_email attribute only when email has been changed
-- user email validation - distribute the logic to the database itself!

DELIMITER //

CREATE TRIGGER reset_email_trigger
BEFORE UPDATE
ON users
FOR EACH ROW
BEGIN
	IF NEW.email <> OLD.email 
		THEN
		SET NEW.valid_email = 0;
	END IF;
	
END;
//

DELIMITER ;

