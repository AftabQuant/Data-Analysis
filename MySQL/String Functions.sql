select * from customers_data.customers_data;

select * from customers_data.customers_data
 where AnnualIncome between "$50,000" and "$55,000"
 order by AnnualIncome desc;
 
select * from customers_data.customers_data
 where TotalChildren in(2,5)
 order by TotalChildren desc;
 
select concat(Prefix," ", FirstName, " ", LastName) as FullName from customers_data.customers_data;
select concat_ws(" ", Prefix, FirstName, LastName) 
as FullName from customers_data.customers_data;

select substring(FirstName, 2,4) 
from customers_data.customers_data;

select replace(FirstName,substring(FirstName, 2,4), "***") 
 from customers_data.customers_data;
 
 
 
 