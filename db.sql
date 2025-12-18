-- Traffic Violation System Database Schema
-- Create database and use it
CREATE DATABASE IF NOT EXISTS traffic_violation_system;
USE traffic_violation_system;

-- Users table (for all system users: admin, police, regular users)
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    role ENUM('admin', 'police', 'user') NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    license_number VARCHAR(50) UNIQUE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Violation types table
CREATE TABLE violation_types (
    violation_type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(100) NOT NULL,
    description TEXT,
    penalty_amount DECIMAL(10,2) NOT NULL,
    points INT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Vehicles table
CREATE TABLE vehicles (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    license_plate VARCHAR(20) UNIQUE NOT NULL,
    owner_user_id INT,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    color VARCHAR(30),
    registration_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (owner_user_id) REFERENCES users(user_id) ON DELETE SET NULL
);

-- Police officers table (extends users with additional info)
CREATE TABLE officers (
    officer_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    badge_number VARCHAR(20) UNIQUE NOT NULL,
    department VARCHAR(100) NOT NULL,
    `rank` VARCHAR(50),
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Violations table (main violations record)
CREATE TABLE violations (
    violation_id INT AUTO_INCREMENT PRIMARY KEY,
    violation_type_id INT NOT NULL,
    officer_id INT NOT NULL,
    vehicle_id INT NOT NULL,
    violation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    location VARCHAR(200) NOT NULL,
    description TEXT,
    penalty_amount DECIMAL(10,2) NOT NULL,
    points_assigned INT NOT NULL,
    status ENUM('pending', 'paid', 'dismissed', 'appeal') DEFAULT 'pending',
    payment_date TIMESTAMP NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (violation_type_id) REFERENCES violation_types(violation_type_id),
    FOREIGN KEY (officer_id) REFERENCES officers(officer_id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
);

-- Create indexes for better performance
CREATE INDEX idx_violations_date ON violations(violation_date);
CREATE INDEX idx_violations_status ON violations(status);
CREATE INDEX idx_violations_vehicle ON violations(vehicle_id);
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_role ON users(role);

-- Insert sample data for testing
-- Sample violation types
INSERT INTO violation_types (type_name, description, penalty_amount, points) VALUES
('Speeding', 'Exceeding the posted speed limit', 150.00, 3),
('Parking Violation', 'Illegal parking in restricted areas', 75.00, 1),
('Red Light Violation', 'Running a red light', 200.00, 4),
('Reckless Driving', 'Dangerous driving behavior', 500.00, 6),
('No Insurance', 'Driving without valid insurance', 300.00, 0),
('Expired Registration', 'Operating vehicle with expired registration', 100.00, 0);

-- Sample users
INSERT INTO users (username, password, email, full_name, role, phone, license_number) VALUES
('admin', 'admin123', 'admin@traffic.gov', 'System Administrator', 'admin', '555-0001', NULL),
('officer1', 'officer123', 'john.smith@traffic.gov', 'Officer John Smith', 'police', '555-0002', NULL),
('officer2', 'officer123', 'jane.doe@traffic.gov', 'Officer Jane Doe', 'police', '555-0003', NULL),
('user1', 'user123', 'john.doe@email.com', 'John Doe', 'user', '555-0004', 'DL123456'),
('user2', 'user123', 'jane.smith@email.com', 'Jane Smith', 'user', '555-0005', 'DL789012');

-- Sample officers (linked to police users)
INSERT INTO officers (user_id, badge_number, department, `rank`, hire_date) VALUES
(2, 'BDG001', 'Traffic Division', 'Sergeant', '2020-01-15'),
(3, 'BDG002', 'Traffic Division', 'Officer', '2021-03-20');

-- Sample vehicles
INSERT INTO vehicles (license_plate, owner_user_id, make, model, year, color, registration_date) VALUES
('ABC123', 4, 'Toyota', 'Camry', 2020, 'Blue', '2020-06-15'),
('XYZ789', 5, 'Honda', 'Civic', 2019, 'Red', '2019-08-20'),
('DEF456', NULL, 'Ford', 'F-150', 2021, 'Black', '2021-03-10');

-- Sample violations
INSERT INTO violations (violation_type_id, officer_id, vehicle_id, location, description, penalty_amount, points_assigned) VALUES
(1, 1, 1, 'Main St & 5th Ave', 'Speeding in school zone', 150.00, 3),
(2, 1, 2, 'Park Ave', 'Parking in no parking zone', 75.00, 1),
(3, 2, 3, 'Highway 101 Exit 15', 'Ran red light at intersection', 200.00, 4);

UPDATE users SET password = SHA2('admin123',256) WHERE username='admin';
UPDATE users SET password = SHA2('officer123',256) WHERE username='officer1';
UPDATE users SET password = SHA2('officer123',256) WHERE username='officer2';
UPDATE users SET password = SHA2('user123',256) WHERE username='user1';
UPDATE users SET password = SHA2('user123',256) WHERE username='user2';

SHOW DATABASES;
SHOW Tables;
