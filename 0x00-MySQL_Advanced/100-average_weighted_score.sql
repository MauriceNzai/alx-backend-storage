#!/usr/bin/env bash

-- stored procedure to compute and store the average weighted score for a student.
-- ComputeAverageScoreForUser takes 1 input: user_id, a users.id value

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
	DECLARE weighted_average FLOAT;
	SET weighted_average = (SELECT SUM(score * weight) / SUM(weight)
		FROM users
		JOIN corrections ON users.id = corrections.user_id
		JOIN projects ON corrections.project_id = projects.id
		WHERE users.id = user_id
	);

	UPDATE users SET average_score = weighted_average WHERE id = user_id;
END;

//

DELIMITER ;
