drop table  if exists Staff cascade; 
create table Staff (
    staff_id serial primary key,
    name text not null,
    salary int,
    email varchar(255),
	birthday timestamp,
	jobtitle_id int
);


insert into Staff(staff_id, name, salary, email, birthday, jobtitle_id) 
values 
(1, 'Иванов Сергей', 100000, 'test@test.ru', '1990-03-03', 1),
(2, 'Петров Пётр', 60000, 'petr@test.ru', '2000-12-01', 7),
(3, 'Сидоров Василий', 80000, 'test@test.ru', '1999-02-04', 6),
(4, 'Максимов Иван', 70000, 'ivan.m@test.ru', '1997-10-02', 4),
(5, 'Попов Иван', 120000, 'popov@test.ru', '2001-04-25', 5);

--select * from Staff;

drop table if exists Jobtitles;
create table Jobtitles(
	jobtitle_id int,
	name text
);

insert into Jobtitles(jobtitle_id, name)
values
(1, 'Разработчик'),
(2, 'Системный аналитик'),
(3, 'Менеджер проектов'), 
(4, 'Системныйадминистратор'),
(5, 'Руководитель группы'),
(6, 'Инженер тестирования'),
(7, 'Сотрудник группы поддержки');

--select * from Jobtitles;


--Напишите запрос, с помощью которого можно найти дубли в поле email из таблицы Sfaff.
select email, count(*) as count_same_email from Staff
group by email
having count(*) > 1;

--Напишите запрос, с помощью которого можно определить возраст каждого сотрудника из таблицы Staff на момент запроса.
SELECT 
	staff_id,
	name,
	extract(year from justify_interval(current_date - birthday)) as age
from staff;


--Напишите запрос, с помощью которого можно определить должность (Jobtitles.name) со вторым по величине уровнем зарплаты.
--Видимо предпологаем, что зарплата у одной должности одинаковая - тогда бы её нужно было в Jobtitles запихнуть

with top2_salary as(
	select 
		salary 
	from Staff
-- join Jobtitles on Staff.jobtitle_id = Jobtitles.jobtitle_id
	group by Staff.salary 
	order by salary desc
	offset 1
	limit 1 
) 
--select * from top2_salary
,jobs_top2 as(
	select 
		jobtitle_id 
	from top2_salary
	join Staff on top2_salary.salary = Staff.salary 
) 
--select * from jobs_top2;
select Jobtitles.name from jobs_top2
join Jobtitles on jobs_top2.jobtitle_id = Jobtitles.jobtitle_id;


