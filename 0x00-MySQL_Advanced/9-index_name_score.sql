-- creates an index on the table names and the first letter of name and score
-- Only the first letter of name and score must be indexed
-- Index is not solution for performance issues, but well used, it’s powerful!

CREATE INDEX idx_name_first_score
ON names ( name(1), score );
