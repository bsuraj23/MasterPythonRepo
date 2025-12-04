-- Create ATTENDANCE table
-- Tracks daily employee attendance

CREATE TABLE ATTENDANCE (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    time_in TIME,
    time_out TIME,
    total_hours DECIMAL(4,2) DEFAULT 0,
    status ENUM('Present', 'Absent', 'Late', 'Half Day', 'Holiday', 'Leave') DEFAULT 'Present',
    notes TEXT,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Unique constraint to prevent duplicate entries for same employee on same date
    CONSTRAINT uk_emp_date UNIQUE (emp_id, attendance_date),
    
    -- Check constraints
    CONSTRAINT chk_attendance_hours CHECK (total_hours >= 0 AND total_hours <= 24),
    CONSTRAINT chk_attendance_times CHECK (time_out IS NULL OR time_in IS NULL OR time_out >= time_in)
);

-- Create indexes
CREATE INDEX idx_attendance_emp ON ATTENDANCE(emp_id);
CREATE INDEX idx_attendance_date ON ATTENDANCE(attendance_date);
CREATE INDEX idx_attendance_status ON ATTENDANCE(status);

-- Show table structure
DESCRIBE ATTENDANCE;