select customerName, city, creditLimit from classic_customers.customers ;

select city, sum(creditLimit), max(creditLimit) from  classic_customers.customers
group by city 
having avg(salesRepEmployeeNumber) > 1500;


-- Create View  
create view country_sum as 
select country, sum(creditLimit), avg(creditLimit) from  classic_customers.customers
group by country 
having avg(salesRepEmployeeNumber) > 1300;

-- Different Joins In MySQL

select  productName, quantityInStock, quantityOrdered from products
inner join `order details`
on products.productCode = `order details`.productCode;

select  productName, quantityInStock, quantityOrdered from products
left join `order details`
on products.productCode = `order details`.productCode;

select  productName, quantityInStock, quantityOrdered from products
right join `order details`
on products.productCode = `order details`.productCode;

select  productName, quantityInStock, quantityOrdered from products
cross join `order details`
on products.productCode = `order details`.productCode;

-- Different Procedure  
Delimiter &&
create procedure get_data()
begin
	select productCode, productName, productLine from products;
end &&
Delimiter ;
call classic_customers.get_data();

Delimiter &&
create procedure get_limit(in var int)
begin
	select productCode, productName, productLine from products limit var ;
end &&
Delimiter ;
call classic_customers.get_limit(5);


DELIMITER &&
CREATE PROCEDURE classic_customers.get_productName(IN x TEXT, OUT var TEXT)
BEGIN
    SELECT productName INTO var 
    FROM classic_customers.products 
    WHERE productCode = x 
    LIMIT 1;
END &&
DELIMITER ;

CALL classic_customers.get_productName('S10_1678', @m);
SELECT @m;


