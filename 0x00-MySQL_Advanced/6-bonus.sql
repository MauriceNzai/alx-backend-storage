-- stored procedure AddBonus that adds a new correction for a student
-- taking 3 inputs 
	-- user_id, a users.id value
	-- project_name, new/already exists projects - if no projects.name in the table, you should create it
	-- score, the score value for the correction

DELIMITER //

CREATE PROCEDURE AddBonus(
	IN user_id INT,
       	IN project_name VARCHAR(255),
       	IN score FLOAT
)
BEGIN
    INSERT INTO projects (name)
    SELECT project_name FROM DUAL

    WHERE NOT EXISTS (SELECT * FROM projects WHERE name = project_name);
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END;

//

DELIMITER ;
