SELECT s.fullname AS Student, t.fullname AS Teacher, d.name AS Discipline
FROM grades g 
JOIN disciplines d ON g.discipline_id = d.id
JOIN teachers t ON d.teacher_id = t.id
JOIN students s ON g.student_id = s.id
WHERE s.id = 1 AND t.id = 1
ORDER BY d.name;