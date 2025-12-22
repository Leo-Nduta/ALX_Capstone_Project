CREATE DATABASE IF NOT EXISTS Bus_Fare_Chart;
USE Bus_Fare_Chart;

CREATE TABLE FARE_CHART (
    id INT AUTO_INCREMENT PRIMARY KEY,
    from_zone INT,
    to_zone INT,
    base_fare INT,
    peak_fare INT,
    currency VARCHAR(10) DEFAULT 'KSH',
    UNIQUE KEY unique_route (from_zone, to_zone);
);

INSERT INTO FARE_CHART (from_zone, to_zone, base_fare, peak_fare)
VALUES
(1, 1, 30, 50),
(1, 2, 50, 70),
(1, 3, 80, 100),
(1, 4, 100, 120),
(2, 1, 50, 80),
(2, 2, 30, 50),
(2, 3, 30, 50),
(2, 4, 50, 70),
(3, 1, 50, 80),
(3, 2, 30, 50),
(3, 3, 30, 50),
(3, 4, 30, 50),
(4, 1, 80, 100),
(4, 2, 50, 70),
(4, 3, 30, 50),
(4, 4, 30, 30);