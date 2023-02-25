SELECT s.fullname AS Name, d.name AS Discipline
FROM grades g 
JOIN disciplines d ON g.discipline_id = d.id
JOIN students s ON g.student_id = s.id 
WHERE s.id = 1
ORDER BY d.name;