from exec_query import execute_query


sql_1 = """SELECT s.fullname, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
LEFT JOIN students s on s.id = g.student_id
GROUP BY s.fullname 
ORDER BY average_grade DESC 
LIMIT 5;"""


sql_2 = """SELECT d.name, s.fullname, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN students s on s.id = g.student_id
JOIN disciplines d ON d.id = g.discipline_id 
WHERE d.id = 1
GROUP BY s.fullname 
ORDER BY average_grade DESC 
LIMIT 1;
"""


sql_3 = """SELECT d.name, gr.name, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN students s on s.id = g.student_id
JOIN disciplines d ON d.id = g.discipline_id 
JOIN [groups] gr ON gr.id = s.group_id 
WHERE d.id = 1
GROUP BY gr.name, d.name 
ORDER BY average_grade DESC;
"""


sql_4 = """SELECT ROUND(AVG(g.grade), 2) AS average_score
FROM grades g;
"""


sql_5 = """SELECT t.fullname, d.name
FROM disciplines d 
JOIN teachers t ON t.id = d.teacher_id 
WHERE t.id = 1;
"""


sql_6 = """SELECT s.fullname AS group_name
FROM students s 
JOIN groups g ON g.id = s.group_id 
WHERE g.id = 1;
"""


sql_7 = """SELECT s.fullname, s.group_id, g.name, d.id, d.name, gra.grade
FROM groups g
JOIN students s ON s.group_id = g.id
JOIN grades gra ON gra.student_id = s.id
JOIN disciplines d ON d.id = gra.discipline_id
WHERE g.id = 1 AND d.id = 1
ORDER BY gra.grade DESC;
"""


sql_8 = """SELECT t.fullname, ROUND(AVG(g.grade), 2) AS AvgGrade
FROM grades g 
JOIN disciplines d ON d.id = g.discipline_id
JOIN teachers t ON t.id = d.teacher_id
WHERE d.teacher_id = 5
ORDER BY AvgGrade DESC;
"""


sql_9 = """SELECT s.fullname AS Name, d.name AS Discipline
FROM grades g 
JOIN disciplines d ON g.discipline_id = d.id
JOIN students s ON g.student_id = s.id 
WHERE s.id = 1
ORDER BY d.name;
"""


sql_10 = """SELECT s.fullname AS Student, t.fullname AS Teacher, d.name AS Discipline
FROM grades g 
JOIN disciplines d ON g.discipline_id = d.id
JOIN teachers t ON d.teacher_id = t.id
JOIN students s ON g.student_id = s.id
WHERE s.id = 1 AND t.id = 1
ORDER BY d.name;
"""


if __name__ == "__main__":
    sqls = [sql_1, sql_2, sql_3, sql_4, sql_5, sql_6, sql_7, sql_8, sql_9, sql_10]

    for sql in sqls:
        print(execute_query(sql))
