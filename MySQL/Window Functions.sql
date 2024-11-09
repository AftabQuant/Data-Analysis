
create view get_job as
select Department, Job_Title, count(EEID) from data_esd.esd
group by Department, Job_Title
order by Department asc;


select Department, Job_Title, rank()
over(partition by EEID) 
from data_esd.esd;
