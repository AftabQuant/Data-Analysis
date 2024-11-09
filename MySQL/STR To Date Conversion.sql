select * from data_esd.esd;

alter table data_esd.esd
 add column nw_date date;
 
SET SQL_SAFE_UPDATES = 0;

UPDATE data_esd.esd
SET nw_date = STR_TO_DATE(Hire_Date, '%m/%d/%y')
WHERE STR_TO_DATE(Hire_Date, '%m/%d/%y') IS NOT NULL;

UPDATE data_esd.esd
SET nw_date = STR_TO_DATE(Hire_Date, '%m/%d/%Y')
WHERE STR_TO_DATE(Hire_Date, '%m/%d/%Y') IS NOT NULL;

alter table data_esd.esd
drop column Hire_Date;

alter table data_esd.esd
change column nw_date Hire_Date date after Age;

set sql_safe_updates = 0;

alter table data_esd.esd
 add column cng_date varchar(15);

update data_esd.esd
 set cng_date = date_format(Hire_Date, '%m-%d-%Y')




