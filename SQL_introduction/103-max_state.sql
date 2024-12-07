-- Display the max temperature of each state (ordered by State name).
SELECT DISTINCT state, MAX(value) as max_temp FROM temperatures
GROUP BY state ORDER BY state LIMIT 3;