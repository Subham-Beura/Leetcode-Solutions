-- Write your PostgreSQL query statement below
select t.id
from weather t
left join weather y
on t.recordDate=y.recordDate+1
where t.temperature>y.temperature