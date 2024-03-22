#!/usr/bin/env bash

-- stored procedure to compute and store the average weighted score for all students.
-- ComputeAverageWeightedScoreForUser takes no input

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE users,
		(SELECT users.id, SUM(score * weight) / SUM(weight) AS weighted_average
		FROM users
		JOIN corrections ON users.id = corrections.user_id
		JOIN projects ON corrections.project_id = projects.id
		GROUP BY users.id
		)
	AS average_w
	SET users.average_score = average_w.weighted_average
	WHERE users.id = average_w.id;
END;

//

DELIMITER ;
