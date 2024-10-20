-- Write your PostgreSQL query statement below
SELECT S.student_id,S.student_name,SU.subject_name,count(E.student_id) AS attended_exams
FROM students S
CROSS JOIN Subjects SU
LEFT JOIN Examinations E
ON S.student_id=E.student_id AND SU.subject_name=E.subject_name
GROUP BY S.student_id,S.student_name,SU.subject_name
