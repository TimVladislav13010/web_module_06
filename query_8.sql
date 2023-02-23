SELECT t.fullname, d.name, ROUND(AVG(g.grade), 2) AS AvgGrade
FROM grades g 
JOIN disciplines d ON d.id = g.discipline_id
JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 5
ORDER BY AvgGrade DESC;

виправити