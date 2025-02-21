## This is the schema for the database

CREATE TABLE Student (
    student_id INT(8) AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(50) UNIQUE NOT NULL,
    first_name VARCHAR(32) NOT NULL,
    last_name VARCHAR(32),
    email VARCHAR(120) UNIQUE NOT NULL,
    clerk_user_id VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT FALSE,
    last_login DATETIME NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);

CREATE TABLE Teacher (
    teacher_id INT(8) AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(50) UNIQUE NOT NULL,
    first_name VARCHAR(32) NOT NULL,
    last_name VARCHAR(32),
    email VARCHAR(120) UNIQUE NOT NULL,
    clerk_user_id VARCHAR(255) NOT NULL,
    role ENUM('admin', 'teacher') NOT NULL,
    is_active BOOLEAN DEFAULT FALSE,
    last_login DATETIME NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);

CREATE TABLE Course (
    course_id INT(8) AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(50) NOT NULL,
    course_code VARCHAR(12) NOT NULL,
    course_description VARCHAR(255),
    capacity INT,
    teacher_id INT(8),
    is_active BOOLEAN DEFAULT FALSE,
    start_date DATETIME NOT NULL,
    end_date DATETIME NOT NULL,
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id)
);

CREATE TABLE Enrollment (
    enrollment_id INT(8) AUTO_INCREMENT PRIMARY KEY,
    student_id INT(8),
    course_id INT(8),
    status ENUM('enrolled', 'cancelled', 'padding') DEFAULT 'enrolled',
    enrollment_date DATETIME NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

CREATE TABLE Exam (
    exam_id INT(8) AUTO_INCREMENT PRIMARY KEY,
    course_id INT(8),
    exam_name VARCHAR(100) NOT NULL,
    exam_description VARCHAR(255),
    start_date DATETIME,
    end_date DATETIME,
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

CREATE TABLE Question (
    question_id INT(8) AUTO_INCREMENT PRIMARY KEY,
    exam_id INT(8),
    question_text VARCHAR(255) NOT NULL,
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (exam_id) REFERENCES Exam(exam_id)
);

CREATE TABLE Answer (
    answer_id INT(8) AUTO_INCREMENT PRIMARY KEY,
    answer_text VARCHAR(255) NOT NULL,
    question_id INT(8),
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (question_id) REFERENCES Question(question_id)
);

CREATE TABLE Student_Answer (
    student_answer_id INT(8) AUTO_INCREMENT PRIMARY KEY,
    student_id INT(8),
    question_id INT(8),
    answer_text VARCHAR(255) NOT NULL,
    second_attempt_answer VARCHAR(255) DEFAULT NULL,
    answer_grade CHAR(1) NOT NULL,
    second_attempt_grade CHAR(1) DEFAULT NULL,
    answer_stage INT,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (question_id) REFERENCES Question(question_id)
);

CREATE TABLE AI_Assessment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    assessment_text VARCHAR(255) NOT NULL,
    student_answer_id INT(8),
    grade CHAR(1),
    FOREIGN KEY (student_answer_id) REFERENCES Student_Answer(student_answer_id)
);



INSERT INTO Student (user_name, first_name, last_name, email, clerk_user_id, is_active, last_login, created_at, updated_at)
VALUES ('Jdoe1', 'John', 'Doe', 'jdoe1@brockport.edu', 'Abc123hashedpassword', TRUE, '2024-09-15', '2023-09-01', '2023-08-15');

INSERT INTO Teacher (user_name, first_name, last_name, email, clerk_user_id, role, is_active, last_login, created_at, updated_at)
VALUES ('Tsmith1', 'Tom', 'Smith', 'Tsmith1@brockport.edu', 'Abc123hashedpassword', 'teacher', TRUE, '2024-09-17', '2023-07-20', '2024-07-22');

INSERT INTO Course (course_name, course_code, course_description, capacity, teacher_id, is_active, start_date, end_date, created_at, updated_at)
VALUES ('Intro to CS', '1', 'A beginner course on CS', 50, 1, TRUE, '2024-11-22', '2024-11-22', '2023-09-01', '2024-09-01');

INSERT INTO Enrollment (student_id, course_id, status, enrollment_date)
VALUES (1, 1, 'enrolled', '2023-09-02');

INSERT INTO Exam (course_id, exam_name, exam_description, start_date, end_date, created_at, updated_at)
VALUES (1, 'Midterm exam 1', 'Covers chapters 1-5 of intro to cs', '2024-10-10', '2024-10-10', '2024-09-01', '2024-10-01');

INSERT INTO Question (exam_id, question_text, created_at, updated_at)
VALUES (1, 'What is a variable in programming', '2024-09-05', '2024-09-06');

INSERT INTO Answer (answer_text, question_id, created_at, updated_at)
VALUES ('A variable stores data values', 1, '2024-09-07', '2024-09-08');

INSERT INTO Student_Answer (student_id, question_id, answer_text, second_attempt_answer, answer_grade, second_attempt_grade, answer_stage)
VALUES (1, 1, 'A variable is a data holder', 'A variable is a data holder', 'S', 'S', 1);

INSERT INTO AI_Assessment (assessment_text, student_answer_id, grade)
VALUES ('Very good answer', 1, 'S');






## PostgreSQL IMPLEMENTATION

-- ENUM types for PostgreSQL
CREATE TYPE role_enum AS ENUM ('admin', 'teacher');
CREATE TYPE enrollment_status_enum AS ENUM ('enrolled', 'cancelled', 'pending');

-- Student Table
CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,
    user_name VARCHAR(50) UNIQUE NOT NULL,
    first_name VARCHAR(32) NOT NULL,
    last_name VARCHAR(32),
    email VARCHAR(120) UNIQUE NOT NULL,
    clerk_user_id VARCHAR(255) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT FALSE,
    last_login TIMESTAMP NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);

-- Teacher Table
CREATE TABLE Teacher (
    teacher_id SERIAL PRIMARY KEY,
    user_name VARCHAR(50) UNIQUE NOT NULL,
    first_name VARCHAR(32) NOT NULL,
    last_name VARCHAR(32),
    email VARCHAR(120) UNIQUE NOT NULL,
    clerk_user_id VARCHAR(255) NOT NULL,
    role role_enum NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT FALSE,
    last_login TIMESTAMP NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);

-- Course Table
CREATE TABLE Course (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(50) NOT NULL,
    course_code VARCHAR(12) NOT NULL,
    course_description VARCHAR(255),
    capacity INT,
    teacher_id INT REFERENCES Teacher(teacher_id) ON DELETE SET NULL,
    is_active BOOLEAN NOT NULL DEFAULT FALSE,
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Enrollment Table
CREATE TABLE Enrollment (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES Student(student_id) ON DELETE CASCADE,
    course_id INT REFERENCES Course(course_id) ON DELETE CASCADE,
    status enrollment_status_enum NOT NULL DEFAULT 'enrolled',
    enrollment_date TIMESTAMP NOT NULL
);

-- Exam Table
CREATE TABLE Exam (
    exam_id SERIAL PRIMARY KEY,
    course_id INT REFERENCES Course(course_id) ON DELETE CASCADE,
    exam_name VARCHAR(100) NOT NULL,
    exam_description VARCHAR(255),
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Question Table
CREATE TABLE Question (
    question_id SERIAL PRIMARY KEY,
    exam_id INT REFERENCES Exam(exam_id) ON DELETE CASCADE,
    question_text VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Answer Table
CREATE TABLE Answer (
    answer_id SERIAL PRIMARY KEY,
    answer_text VARCHAR(255) NOT NULL,
    question_id INT REFERENCES Question(question_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Student Answer Table
CREATE TABLE Student_Answer (
    student_answer_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES Student(student_id) ON DELETE CASCADE,
    question_id INT REFERENCES Question(question_id) ON DELETE CASCADE,
    answer_text VARCHAR(255) NOT NULL,
    second_attempt_answer VARCHAR(255) DEFAULT NULL,
    answer_grade CHAR(1) NOT NULL,
    second_attempt_grade CHAR(1) DEFAULT NULL,
    answer_stage INT
);

-- AI Assessment Table
CREATE TABLE AI_Assessment (
    id SERIAL PRIMARY KEY,
    assessment_text VARCHAR(255) NOT NULL,
    student_answer_id INT REFERENCES Student_Answer(student_answer_id) ON DELETE CASCADE,
    grade CHAR(1)
);


-- Insert into Student
INSERT INTO Student (user_name, first_name, last_name, email, clerk_user_id, is_active, last_login, created_at, updated_at)
VALUES ('Jdoe1', 'John', 'Doe', 'jdoe1@brockport.edu', 'Abc123hashedpassword', TRUE, '2024-09-15 00:00:00', '2023-09-01 00:00:00', '2023-08-15 00:00:00');

-- Insert into Teacher
INSERT INTO Teacher (user_name, first_name, last_name, email, clerk_user_id, role, is_active, last_login, created_at, updated_at)
VALUES ('Tsmith1', 'Tom', 'Smith', 'Tsmith1@brockport.edu', 'Abc123hashedpassword', 'teacher', TRUE, '2024-09-17 00:00:00', '2023-07-20 00:00:00', '2024-07-22 00:00:00');

INSERT INTO Teacher (user_name, first_name, last_name, email, clerk_user_id, role, is_active, last_login, created_at, updated_at)
VALUES ('Hgeman', 'gerald', 'Gemany', 'hgeman@brockport.edu', 'Abc123hashedpassword', 'admin', TRUE, '2024-09-17 00:00:00', '2023-07-20 00:00:00', '2024-07-22 00:00:00');

-- Insert into Course (assuming the teacher ID = 1)
INSERT INTO Course (course_name, course_code, course_description, capacity, teacher_id, is_active, start_date, end_date, created_at, updated_at)
VALUES ('Intro to CS', 'CS101', 'A beginner course on CS', 50, 1, TRUE, '2024-11-22 00:00:00', '2024-11-22 00:00:00', '2023-09-01 00:00:00', '2024-09-01 00:00:00');

-- Insert into Enrollment (assuming student ID = 1, course ID = 1)
INSERT INTO Enrollment (student_id, course_id, status, enrollment_date)
VALUES (1, 1, 'enrolled', '2023-09-02 00:00:00');

-- Insert into Exam (assuming course ID = 1)
INSERT INTO Exam (course_id, exam_name, exam_description, start_date, end_date, created_at, updated_at)
VALUES (1, 'Midterm Exam 1', 'Covers chapters 1-5 of intro to CS', '2024-10-10 00:00:00', '2024-10-10 00:00:00', '2024-09-01 00:00:00', '2024-10-01 00:00:00');

-- Insert into Question (assuming exam ID = 1)
INSERT INTO Question (exam_id, question_text, created_at, updated_at)
VALUES (1, 'What is a variable in programming?', '2024-09-05 00:00:00', '2024-09-06 00:00:00');

-- Insert into Answer (assuming question ID = 1)
INSERT INTO Answer (answer_text, question_id, created_at, updated_at)
VALUES ('A variable stores data values.', 1, '2024-09-07 00:00:00', '2024-09-08 00:00:00');

-- Insert into Student_Answer (assuming student ID = 1, question ID = 1)
INSERT INTO Student_Answer (student_id, question_id, answer_text, second_attempt_answer, answer_grade, second_attempt_grade, answer_stage)
VALUES (1, 1, 'A variable is a data holder', 'A variable is a data holder', 'S', 'S', 1);

-- Insert into AI_Assessment (assuming student_answer_id = 1)
INSERT INTO AI_Assessment (assessment_text, student_answer_id, grade)
VALUES ('Very good answer', 1, 'S');

