Delimiter &&
-- Without Parameter 
create procedure get_data()
begin 
	select * from data_esd.esd;
end &&
Delimiter ;

--  In Operator
Delimiter &&
create procedure get_limit(in var int)
begin 
	select * from data_esd.esd limit var;
end &&
Delimiter ;

-- Out Operator
Delimiter &&
create procedure get_max(out var int)
 begin
	 select max(Salary) into var from data_esd.esd;
 end &&
 Delimiter ;


-- In Out Operator
Delimiter &&
create procedure get_name(inout var int)
 begin
	select Full_Name from esd where Full_Name = var;
 end &&
Delimiter ;

set @m = 125;
call get_name(@m);
select @m;

call get_data();
call get_limit(5);
call get_max(@z);
select @z;