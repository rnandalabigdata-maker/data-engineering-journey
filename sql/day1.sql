-- My first table
CREATE TABLE cities (
    id      INT PRIMARY KEY,
    city    TEXT NOT NULL,
    country TEXT NOT NULL
);

INSERT INTO cities VALUES
    (1, 'Dubai', 'UAE'),
    (2, 'Abu Dhabi', 'UAE'),
    (3, 'Mumbai', 'India'),
    (4, 'Bengaluru', 'India'),
    (5, 'Hyderabad', 'India');

SELECT country, COUNT(*) AS total_cities
FROM cities
GROUP BY country
ORDER BY total_cities DESC;