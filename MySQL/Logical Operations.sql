use customers_data;
select * from customers_data;

select FirstName, LastName, BirthDate, AnnualIncome from customers_data where FirstName = "JON";

select FirstName, LastName, BirthDate, AnnualIncome from customers_data 
	where FirstName = "JON" and HomeOwner = "Y";

select FirstName, LastName, BirthDate, AnnualIncome from customers_data
	where MaritalStatus = "M" or AnnualIncome >= 60000;

select FirstName, LastName, BirthDate, AnnualIncome from customers_data 
	where MaritalStatus = "M" or AnnualIncome >= 60000 and LastName = "TORRES";
    
select * from customers_data where FirstName like "%GE";
select * from customers_data where FirstName like "%GE" and LastName like "%D";
        
select * from customers_data where FirstName like "%GE" and LastName like "%D"
order by AnnualIncome desc;

select * from customers_data
	order by AnnualIncome, FirstName desc;
    
select * from customers_data
	order by AnnualIncome desc, FirstName asc;

select * from customers_data
	limit 3,13;
        
        
        
        