select truncate(sum(amount),0) from sakila.payment;

select count(payment_id) from sakila.payment;

select avg(rental_id) from sakila.payment;

select max(amount) as max_amount from sakila.payment;

select datediff(last_update, payment_date) from sakila.payment;

select  dayname(payment_date) as day_name from sakila.payment;
