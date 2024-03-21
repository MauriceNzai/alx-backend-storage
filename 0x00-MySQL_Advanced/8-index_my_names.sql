-- creates an index on the table names and the first letter of name.
-- Only the first letter of name must be indexed
-- Index is not solution for performance issues, but well used, it’s powerful!

CREATE INDEX idx_name_first
ON names ( name(1) );
