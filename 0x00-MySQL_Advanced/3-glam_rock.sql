-- lists all bands with main style as Glam rock, ranked by their longevity
-- Column names must be: band_name and lifespan (in years until 2022)
-- use attributes formed and split for computing the lifespan
-- script can be executed on any database

SELECT band_name, IFNULL(split, 2022) - formed AS lifespan
FROM metal_bands
WHERE FIND_IN_SET("Glam rock", style)
ORDER BY lifespan DESC;
