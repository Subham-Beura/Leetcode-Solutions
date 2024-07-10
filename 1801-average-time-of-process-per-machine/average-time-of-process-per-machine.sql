-- Write your PostgreSQL query statement below
select s.machine_id,round(avg(e.timestamp -s.timestamp )::numeric,3) as processing_time
from activity s
inner join activity e
on s.machine_id=e.machine_id and s.process_id =e.process_id
and s.activity_type= 'start' 
and e.activity_type='end' and e.timestamp is not null
group by s.machine_id