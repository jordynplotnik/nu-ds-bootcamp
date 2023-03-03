-- List the employee number, last name, first name, sex, and salary of each employee 

SELECT A.EMP_NO,
B.FIRST_NAME,
B.LAST_NAME,
B.SEX,
A.SALARY
FROM SALARIES A
LEFT JOIN EMPLOYEES B
ON A.EMP_NO = B.EMP_NO;

-- List the first name, last name, and hire date for the employees who were hired in 1986 (2 points)

SELECT 
FIRST_NAME,
LAST_NAME,
HIRE_DATE
FROM EMPLOYEES 
WHERE HIRE_DATE BETWEEN '1986-01-01' AND '1986-12-31';

-- List the manager of each department along with their department number, department name, employee number, last name, and first name (2 points)

SELECT 
A.DEPT_NO,
C.DEPT_NAME,
A.EMP_NO,
B.FIRST_NAME,
B.LAST_NAME
FROM DEPT_MANAGER A
LEFT JOIN EMPLOYEES B
ON A.EMP_NO = B.EMP_NO
LEFT JOIN DEPARTMENTS C
ON A.DEPT_NO = C.DEPT_NO
WHERE HIRE_DATE BETWEEN '1986-01-01' AND '1986-12-31';

-- List the department number for each employee along with that employee’s employee number, last name, first name, and department name (2 points)

SELECT A.EMP_NO,
A.LAST_NAME,
A.FIRST_NAME,
C.DEPT_NAME
FROM EMPLOYEES A
LEFT JOIN DEPT_EMP B
ON A.EMP_NO = B.EMP_NO
LEFT JOIN DEPARTMENTS C
ON B.DEPT_NO = C.DEPT_NO;

-- List first name, last name, and sex of each employee whose first name is Hercules and whose last name begins with the letter B (2 points)

SELECT 
FIRST_NAME,
LAST_NAME,
SEX
FROM EMPLOYEES 
WHERE FIRST_NAME LIKE 'Hercules'
AND LAST_NAME LIKE 'B%';

-- List each employee in the Sales department, including their employee number, last name, and first name (2 points)

SELECT 
A.EMP_NO,
A.LAST_NAME,
A.FIRST_NAME,
C.DEPT_NAME
FROM EMPLOYEES A
LEFT JOIN DEPT_EMP B
ON A.EMP_NO = B.EMP_NO
LEFT JOIN DEPARTMENTS C
ON B.DEPT_NO = C.DEPT_NO
WHERE DEPT_NAME = 'Sales';

-- List each employee in the Sales and Development departments, including their employee number, last name, first name, and department name (4 points)

SELECT 
A.EMP_NO,
A.LAST_NAME,
A.FIRST_NAME,
C.DEPT_NAME
FROM EMPLOYEES A
LEFT JOIN DEPT_EMP B
ON A.EMP_NO = B.EMP_NO
LEFT JOIN DEPARTMENTS C
ON B.DEPT_NO = C.DEPT_NO
WHERE DEPT_NAME = 'Sales'
OR DEPT_NAME = 'Development';

-- List the frequency counts, in descending order, of all the employee last names (that is, how many employees share each last name) (4 points)

SELECT 
LAST_NAME,
COUNT(EMP_NO) AS FREQUENCY
FROM EMPLOYEES 
GROUP BY LAST_NAME
ORDER BY FREQUENCY DESC;
