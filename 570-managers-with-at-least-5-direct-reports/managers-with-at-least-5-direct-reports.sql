-- Write your PostgreSQL query statement below
SELECT EL.name FROM Employee EL
LEFT JOIN Employee ER
ON EL.id=ER.managerId
GROUP BY EL.id,EL.name
HAVING COUNT(ER.id)>=5;