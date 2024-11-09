use classic_customers;

-- Inner Join --  
select products.productName, sum(products.MSRP)  from products
inner join `order details`
on products.productCode = `order details`.productCode
group by products.productName;

-- Left Joins
select * from products
left join `order details`
on products.productCode = `order details`.productCode;

-- Right Joins
select * from products
right join `order details`
on products.productCode = `order details`.productCode;

--  Cross Joins
select * from products
cross join `order details`
on products.productCode = `order details`.productCode;
