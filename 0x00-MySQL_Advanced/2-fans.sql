-- Import table dump
-- Ranks country origins of bands, ordered by the number of (non-unique) fans
-- Use origin and nb_fans colunms
-- script can be executed on any database

SELECT `origin`, SUM(`fans`) as `nb_fans` FROM `metal_bands` 
GROUP BY `origin`
ORDER BY nb_fans DESC;
