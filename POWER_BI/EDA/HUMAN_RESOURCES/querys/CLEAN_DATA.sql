
SELECT * FROM hr;

ALTER TABLE hr
CHANGE COLUMN ï»¿id emp_id VARCHAR(20) NULL;

DESCRIBE hr;

SELECT birthdate FROM hr;

SET sql_safe_updates = 0;

UPDATE hr
SET birthdate = CASE
	WHEN birthdate LIKE '%/%' THEN date_format(str_to_date(birthdate, '%m/%d/%Y'), '%Y-%m-%d')
    WHEN birthdate LIKE '%-%' THEN date_format(str_to_date(birthdate, '%m-%d-%Y'), '%Y-%m-%d')
    ELSE NULL
END;

ALTER TABLE hr
MODIFY COLUMN birthdate DATE;

UPDATE hr
SET hire_date = CASE
	WHEN hire_date LIKE '%/%' THEN date_format(str_to_date(hire_date, '%m/%d/%Y'), '%Y-%m-%d')
    WHEN hire_date LIKE '%-%' THEN date_format(str_to_date(hire_date, '%m-%d-%Y'), '%Y-%m-%d')
    ELSE NULL
END;

ALTER TABLE hr
MODIFY COLUMN hire_date DATE;

UPDATE hr
SET termdate = date(STR_TO_DATE(TRIM(termdate), '%Y-%m-%d %H:%i:%s'))
WHERE termdate IS NOT NULL AND TRIM(termdate) != ' ';

update hrhr
set  termdate = NULL 
WHERE termdate is null or termdate = '';

select termdate from hr;

ALTER TABLE hr
MODIFY COLUMN termdate DATE;

describe hr;

alter table hr
add column age int ;

select * from hr;

update hr 
set age = timestampdiff(year, birthdate, curdate());
select birthdate from hr ;

select birthdate from hr 
order by birthdate desc;

select count(*) from hr where age < 18;
