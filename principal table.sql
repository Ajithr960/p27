CREATE TABLE principal (
    sno INTEGER PRIMARY KEY AUTOINCREMENT,
    teacherId TEXT UNIQUE,
    teacherName TEXT,
    teacherSalary FLOT,
    teacherJoiningDate DATE
);
