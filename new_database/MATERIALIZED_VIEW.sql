create materialized view num_questions
refresh complete on commit
as
select username, count(c.id)
from utilizator u 
join legatura l on l.id_parinte = u.id
join copil c on l.id_copil = c.id
group by username
order by count(c.id) asc;
