# Write your MySQL query statement below
# using CET

with cet as (
    select distinct class, count(*) over (partition by class) as cnt
    from courses
)

select class
from cet
where cnt >= 5
