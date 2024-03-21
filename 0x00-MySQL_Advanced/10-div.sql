#!/bin/usr/env bash
-- function that divides (and returns) the 1st by the 2nd number
-- or returns 0 if the second number is equal to 0.
-- takes 2 arguments: a, INT and b, INT

DELIMITER //

DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    DECLARE result FLOAT;
    IF b = 0 THEN
        SET result = 0;
    ELSE
        SET result = a / b;
    END IF;
    RETURN result;
END;
//

DELIMITER ;
