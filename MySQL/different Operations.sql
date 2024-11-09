select min(Smoking_Prevalence) from data_smoking.smoking_data;
select max(Smoking_Prevalence) from data_smoking.smoking_data;


select min(Year) from data_smoking.smoking_data;
select max(Year) from data_smoking.smoking_data;

select concat(Prefix, " ", FirstName, " ", LastName) 
as Full_Name from customers_data.customers_data;

select sum(TotalChildren) as AnnualSum
	from customers_data.customers_data;
select avg(TotalChildren) as AnnualSum
	from customers_data.customers_data;
    
select * from customers_data.customers_data
where Occupation in('Clerical', 'Management');

select FirstName from customers_data.customers_data
where CustomerKey between 11010 and 11200;