show databases;




CREATE database Student_Management; 

USE Student_Management;

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT CHECK (age >= 16),
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) UNIQUE,
    department_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

CREATE TABLE departments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL UNIQUE
);


CREATE TABLE courses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    credits INT CHECK (credits BETWEEN 1 AND 10)
);


CREATE TABLE enrollments (
    student_id INT,
    course_id INT,
    enrollment_date DATE DEFAULT (CURRENT_DATE),
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
);

CREATE TABLE teachers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) UNIQUE,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

CREATE TABLE subjects (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id) ON DELETE SET NULL
);






show tables;

INSERT INTO departments (name) VALUES 
('Computer Science'),
('Mechanical Engineering'),
('Electronics'),
('Civil Engineering');
 
 INSERT INTO students (name, age, email, phone, department_id) VALUES 
('Ali', 22, 'ali@email.com', '9876543210', 1),
('Simran', 21, 'simran@email.com', '9876543211', 2),
('Damian Blackwell', 23, 'damian@email.com', '9876543212', 1),
('Isla Valentine', 20, 'isla@email.com', '9876543213', 3);


INSERT INTO courses (name, credits) VALUES 
('Data Structures', 4),
('Machine Learning', 3),
('Thermodynamics', 3),
('Structural Analysis', 4);


INSERT INTO enrollments (student_id, course_id) VALUES 
(1, 1), --  -- Ali -> Data Structures
(1, 2), -- Ali -> Machine Learning
(2, 3), -- Simran -> Thermodynamics
(3, 1), -- Damian -> Data Structures
(4, 4); -- Isla -> Structural Analysis


INSERT INTO teachers (name, email, phone, department_id) VALUES 
('Dr. Sharma', 'sharma@email.com', '9876543214', 1),
('Prof. Rao', 'rao@email.com', '9876543215', 2),
('Dr. Mehta', 'mehta@email.com', '9876543216', 3);



INSERT INTO subjects (name, teacher_id) VALUES 
('Data Structures', 1), 
('Machine Learning', 1),
('Thermodynamics', 2),
('Structural Analysis', 3);


show tables;

select * from students;
select * from departments;
select * from courses;
select * from enrollments;
select * from subjects;
select * from teachers;


-- Queries for Student Management System


select  students.name ,students.age, students.email,students.department as department
from students
join department on students.department_id = department_id;


--  Fetch All Students with Their Departments

SELECT students.name, students.age, students.email, departments.name AS department 
FROM students 
JOIN departments ON students.department_id = departments.id;




-- SQL JOIN Functions: Combining Data from Multiple Tables

-- INNER JOIN (Only Matching Records)

SELECT students.name, students.age, departments.name AS department
FROM students
INNER JOIN departments ON students.department_id = departments.id;


-- LEFT JOIN (All Records from Left + Matching Records from Right)

SELECT students.name, students.age, departments.name AS department
FROM students
LEFT JOIN departments ON students.department_id = departments.id;


-- RIGHT JOIN (All Records from Right + Matching from Left)

SELECT students.name, students.age, departments.name AS department
FROM students
RIGHT JOIN departments ON students.department_id = departments.id;


-- FULL JOIN (All Records from Both Tables)
SELECT students.name, students.age, departments.name AS department
FROM students
LEFT JOIN departments ON students.department_id = departments.id
UNION
SELECT students.name, students.age, departments.name AS department
FROM students
RIGHT JOIN departments ON students.department_id = departments.id;


-- CROSS JOIN (All Possible Combinations)
SELECT students.name, departments.name AS department
FROM students
CROSS JOIN departments;


--  Self JOIN (When a Table Joins Itself)
SELECT e1.name AS employee, e2.name AS manager
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.id;


-- NATURAL JOIN (Auto Matching Columns)
SELECT students.name, students.age, departments.name AS department
FROM students
NATURAL JOIN departments;


