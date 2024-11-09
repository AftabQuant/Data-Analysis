use data_esd;

select Full_Name, Job_Title,
case
	when age >=50 then " Quinquagenarian"
    when age <=25 then "Fresher"
    else "Young Man"
end as Age_Name
from esd;

set SQL_SAFE_UPDATES = 0;
alter table esd
add column Age_Name varchar(20);

update esd
set Age_Name = 
  case
		when age >=50 then " Quinquagenarian"
    when age <=25 then "Fresher"
    else "Young Man"
end ;

alter table esd
add column Salary int;

alter table esd
change column `Business Unit` Business_Unit text;


set SQL_SAFE_UPDATES = 0;

update esd
set Salary = 
	cast(replace(replace(`Annual Salary`, '$', ''),',','')as unsigned);