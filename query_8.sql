SELECT t.fullname, ROUND(AVG(g.grade), 2) AS AvgGrade
FROM grades g 
JOIN disciplines d ON d.id = g.discipline_id
JOIN teachers t ON t.id = d.teacher_id
WHERE d.teacher_id = 5
ORDER BY AvgGrade DESC;