use copy_data;

create table auto_incr(
 emp_id int auto_increment,
 name varchar(10),
 primary key(emp_id)
);

drop table auto_incr;

insert into auto_incr(name)
values ('Aftab'),
('Imran'), 
('Ariful');

alter table auto_incr
-- add column age int not null,
add column marks float not null;

--  Drop Column From A Table
alter table auto_incr
drop column marks;
--  