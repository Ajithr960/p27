CREATE TABLE teacher (
    sno INTEGER PRIMARY KEY AUTOINCREMENT,
    teacherId CHAR UNIQUE,
    teacherName VARCHAR (20),
    teacherSalary FLOAT,
    teacherJoiningDate DATE
);
