-- creates a trigger to decrease quantity of item after adding a new order.
-- Quantity in the table items can be negative.
-- Updating multiple tables for one action can generate issue,
-- Create triggers and let MySQL do it for you!

DELIMITER //

CREATE TRIGGER item_decrease_trigger
AFTER INSERT
ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END;
//
