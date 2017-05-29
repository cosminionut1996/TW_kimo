create materialized view num_questions
refresh complete on commit
as
select user_id, count(id)
from questions
group by user_id;
