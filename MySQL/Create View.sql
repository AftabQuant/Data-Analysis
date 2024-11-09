-- Create View

create view Department as
select Department, avg(Salary), count(EEID)
from data_esd.esd
group by Department; 