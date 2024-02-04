CREATE TABLE admin (
    sno INTEGER PRIMARY KEY AUTOINCREMENT,
    adminId TEXT UNIQUE,
    adminName TEXT,
    adminPassword TEXT
);

-- Create admin_permissions table
CREATE TABLE admin_permissions (
    adminId TEXT UNIQUE,
    can_create_teacher BOOLEAN,
    can_create_student BOOLEAN,
    can_create_principal BOOLEAN,
    can_create_admin BOOLEAN,
    FOREIGN KEY (adminId) REFERENCES admin(adminId)
);

-- Insert an admin with permissions
INSERT INTO admin (adminId, adminName, adminPassword) VALUES ('A001', 'Admin A', 'admin_password');

-- Grant permissions to the admin
INSERT INTO admin_permissions (adminId, can_create_teacher, can_create_student, can_create_principal, can_create_admin)
VALUES ('A001', 1, 1, 1, 1);
