select Job_Title, count(EEID), avg(Salary) from data_esd.esd
 group by Job_Title
 order by count(EEID) asc;
 
select Job_Title, count(EEID), avg(Salary) from data_esd.esd
 group by Job_Title
 having avg(Salary) > 75000;