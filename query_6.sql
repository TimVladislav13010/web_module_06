SELECT s.fullname AS group_name
FROM students s 
JOIN groups g ON g.id = s.group_id 
WHERE g.id = 1;