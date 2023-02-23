SELECT s.fullname, s.group_id, g.name, d.id, d.name, gra.grade
FROM groups g
JOIN students s ON s.group_id = g.id
JOIN grades gra ON gra.student_id = s.id
JOIN disciplines d ON d.id = gra.discipline_id
WHERE g.id = 1 AND d.id = 1
ORDER BY gra.grade DESC;