-- QUESTIONS

-- 1. What is the gender breakdown of employees in the company?
SELECT gender,count(*)
FROM hr 
WHERE termdate IS NULL AND age >=18
GROUP BY gender;
-- 2. What is the race/ethnicity breakdown of employees in the company?
SELECT race, count(*) race_count FROM hr
WHERE age >= 18 AND termdate IS NULL 
GROUP BY race;
-- 3. What is the age distribution of employees in the company?
SELECT MIN(age), MAX(age) 
FROM hr 
WHERE age >=18 AND termdate IS NULL;

SELECT
    CASE 
	 WHEN age >= 21 and age <= 30 then "21-30"
     when age >= 31 and age <= 40 then "31-40"
     when age >= 41 and age <= 50 then "41-50"
     when age >= 51 and age <= 60 then "51-60"
	ELSE
		age = "61+"
	END AS age_distribution,
    count(*) as count
	FROM hr
    WHERE age >=18 AND termdate IS NULL
    GROUP BY age_distribution;

-- 4. How many employees work at headquarters versus remote locations?

select sum(case when location like "H%" then 1  end) as num_headquarters_jobs,
	   sum(case when location like "R%" then 1 end) as num_remote_jobs
from hr
where age >=18 and termdate is null;

-- 5. What is the average length of employment for employees who have been terminated?
select
	# first convert the diff to year and then obtain the AVG
	round(avg(datediff(termdate,hire_date)/365),0) as avg_employment 
from hr
where termdate <= curdate()and age>=18;

-- 6. How does the gender distribution vary across departments and job titles?
select 
	department,jobtitle,
	coalesce(sum(case when gender like "F%" then 1 end),0) as female_by_departement,
    coalesce(sum(case when gender like "M%" then 1 end),0) as male_by_department,
	coalesce(sum(case when gender like "N%" then 1 end),0) as other
from hr 
where age>=18 and termdate is null
group by department,jobtitle;


-- 7. What is the distribution of job titles across the company?

select jobtitle,count(*) as emp_by_jobtitle
from hr 
where age>=18 and termdate is null
group by jobtitle
order by emp_by_jobtitle desc;

-- 8. Which department has the highest turnover rate?
 select 
 department,
 total_count,
 count_term,
 (count_term / total_count) as terminated_rate
 from (
	select
	department,
    count(*) as total_count,
    count(case when termdate is not null and termdate <= curdate() then 1 end) as count_term
    from hr
    where age>=18
    group by department
 ) as subquery
 order by terminated_rate desc;
 

-- 9. What is the distribution of employees across locations by state?

select location_state,count(*) as num_employees 
from hr 
where termdate is not null and age>=18
group by location_state
order by num_employees desc;

-- 10. How has the company's employee count changed over time based on hire and term dates?
SELECT 
    YEAR(hire_date) AS year, 
    COUNT(*) AS hires, 
    SUM(CASE WHEN termdate IS NOT NULL AND termdate <= CURDATE() THEN 1 ELSE 0 END) AS terminations, 
    COUNT(*) - SUM(CASE WHEN termdate IS NOT NULL AND termdate <= CURDATE() THEN 1 ELSE 0 END) AS net_change,
    ROUND(((COUNT(*) - SUM(CASE WHEN termdate IS NOT NULL AND termdate <= CURDATE() THEN 1 ELSE 0 END)) / COUNT(*) * 100),2) AS net_change_percent
FROM 
    hr
WHERE age >= 18
GROUP BY 
    YEAR(hire_date)
ORDER BY 
    YEAR(hire_date) ASC;

-- 11. What is the tenure ratio for each department?
select department,
	round(avg(datediff(termdate,hire_date)/365),0) as tenure_ratio
from hr
where age>=18 and termdate < curdate() and termdate is not null
group by department
order by tenure_ratio desc;


select * from hr;

select concat(first_name," ",last_name) as full_name, age, jobtitle from hr;