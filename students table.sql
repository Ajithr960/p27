-- Create students table
CREATE TABLE students (
    sno INTEGER PRIMARY KEY AUTOINCREMENT,
    studentId TEXT UNIQUE,
    studentName TEXT,
    pythonMark INTEGER,
    MathMark INTEGER,
    PhysicsMark INTEGER
);

-- 1. Create a student
INSERT INTO students (studentId, studentName, pythonMark, MathMark, PhysicsMark)
VALUES ('S001', 'John Doe', 90, 85, 75);

-- 2. Read students
SELECT * FROM students;

-- 3. Update a student
UPDATE students
SET studentName = 'John Smith'
WHERE studentId = 'S001';

-- 4. Delete a student
DELETE FROM students
WHERE studentId = 'S001';
