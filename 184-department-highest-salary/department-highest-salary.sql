# Write your MySQL query statement below

with temp_table as (
    select e.name as Employee, d.name as Department, salary as Salary, 
    RANK() over (partition by e.departmentid order by salary desc) as rnk
    from Employee e, Department d
    where e.departmentid = d.id
)

-- select * from temp_table

select Employee, Department, Salary
from temp_table
where rnk = 1
