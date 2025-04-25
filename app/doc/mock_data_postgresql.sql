-- Mock Data Generation for PostgreSQL

-- Students
INSERT INTO "Student" (user_name, first_name, last_name, email, clerk_user_id, is_active, last_login, created_at, updated_at) VALUES
('Jdoe1', 'John', 'Doe', 'jdoe1@brockport.edu', 'Abc123hashedpassword', TRUE, TIMESTAMP '2024-09-15', TIMESTAMP '2023-09-01', TIMESTAMP '2023-08-15'),
('Sjohnson2', 'Sarah', 'Johnson', 'sjohnson2@brockport.edu', 'Def456hashedpassword', TRUE, TIMESTAMP '2024-09-16', TIMESTAMP '2023-09-02', TIMESTAMP '2023-08-16'),
('Mwilliams3', 'Michael', 'Williams', 'mwilliams3@brockport.edu', 'Ghi789hashedpassword', TRUE, TIMESTAMP '2024-09-17', TIMESTAMP '2023-09-03', TIMESTAMP '2023-08-17'),
('Emartinez4', 'Emily', 'Martinez', 'emartinez4@brockport.edu', 'Jkl012hashedpassword', TRUE, TIMESTAMP '2024-09-18', TIMESTAMP '2023-09-04', TIMESTAMP '2023-08-18'),
('Rgarcia5', 'Robert', 'Garcia', 'rgarcia5@brockport.edu', 'Mno345hashedpassword', TRUE, TIMESTAMP '2024-09-19', TIMESTAMP '2023-09-05', TIMESTAMP '2023-08-19'),
('Lbrown6', 'Lisa', 'Brown', 'lbrown6@brockport.edu', 'Pqr678hashedpassword', TRUE, TIMESTAMP '2024-09-20', TIMESTAMP '2023-09-06', TIMESTAMP '2023-08-20'),
('Dmiller7', 'David', 'Miller', 'dmiller7@brockport.edu', 'Stu901hashedpassword', TRUE, TIMESTAMP '2024-09-21', TIMESTAMP '2023-09-07', TIMESTAMP '2023-08-21'),
('Jdavis8', 'Jennifer', 'Davis', 'jdavis8@brockport.edu', 'Vwx234hashedpassword', TRUE, TIMESTAMP '2024-09-22', TIMESTAMP '2023-09-08', TIMESTAMP '2023-08-22'),
('Trodriguez9', 'Thomas', 'Rodriguez', 'trodriguez9@brockport.edu', 'Yza567hashedpassword', TRUE, TIMESTAMP '2024-09-23', TIMESTAMP '2023-09-09', TIMESTAMP '2023-08-23'),
('Mwilson10', 'Mary', 'Wilson', 'mwilson10@brockport.edu', 'Bcd890hashedpassword', TRUE, TIMESTAMP '2024-09-24', TIMESTAMP '2023-09-10', TIMESTAMP '2023-08-24');

-- Teachers
INSERT INTO "Teacher" (user_name, first_name, last_name, email, clerk_user_id, role, is_active, last_login, created_at, updated_at) VALUES
('Tsmith1', 'Tom', 'Smith', 'Tsmith1@brockport.edu', 'Abc123hashedpassword', 'teacher', TRUE, TIMESTAMP '2024-09-17', TIMESTAMP '2023-07-20', TIMESTAMP '2024-07-22'),
('Janderson2', 'Jane', 'Anderson', 'janderson2@brockport.edu', 'Def456hashedpassword', 'teacher', TRUE, TIMESTAMP '2024-09-18', TIMESTAMP '2023-07-21', TIMESTAMP '2024-07-23'),
('Rthomas3', 'Richard', 'Thomas', 'rthomas3@brockport.edu', 'Ghi789hashedpassword', 'teacher', TRUE, TIMESTAMP '2024-09-19', TIMESTAMP '2023-07-22', TIMESTAMP '2024-07-24'),
('Lmoore4', 'Laura', 'Moore', 'lmoore4@brockport.edu', 'Jkl012hashedpassword', 'teacher', TRUE, TIMESTAMP '2024-09-20', TIMESTAMP '2023-07-23', TIMESTAMP '2024-07-25'),
('Staylor5', 'Steven', 'Taylor', 'staylor5@brockport.edu', 'Mno345hashedpassword', 'teacher', TRUE, TIMESTAMP '2024-09-21', TIMESTAMP '2023-07-24', TIMESTAMP '2024-07-26'),
('Awhite6', 'Amanda', 'White', 'awhite6@brockport.edu', 'Pqr678hashedpassword', 'teacher', TRUE, TIMESTAMP '2024-09-22', TIMESTAMP '2023-07-25', TIMESTAMP '2024-07-27'),
('Pjackson7', 'Paul', 'Jackson', 'pjackson7@brockport.edu', 'Stu901hashedpassword', 'teacher', TRUE, TIMESTAMP '2024-09-23', TIMESTAMP '2023-07-26', TIMESTAMP '2024-07-28'),
('Cmartin8', 'Catherine', 'Martin', 'cmartin8@brockport.edu', 'Vwx234hashedpassword', 'teacher', TRUE, TIMESTAMP '2024-09-24', TIMESTAMP '2023-07-27', TIMESTAMP '2024-07-29'),
('Dthompson9', 'Daniel', 'Thompson', 'dthompson9@brockport.edu', 'Yza567hashedpassword', 'teacher', TRUE, TIMESTAMP '2024-09-25', TIMESTAMP '2023-07-28', TIMESTAMP '2024-07-30'),
('Hclark10', 'Helen', 'Clark', 'hclark10@brockport.edu', 'Bcd890hashedpassword', 'teacher', TRUE, TIMESTAMP '2024-09-26', TIMESTAMP '2023-07-29', TIMESTAMP '2024-07-31');

-- Courses
INSERT INTO "Course" (course_name, course_code, course_description, capacity, teacher_id, is_active, start_date, end_date, created_at, updated_at) VALUES
('Intro to CS', 'CSC101', 'A beginner course on Computer Science fundamentals', 50, 1, TRUE, DATE '2024-09-01', DATE '2024-12-15', TIMESTAMP '2023-09-01', TIMESTAMP '2024-09-01'),
('Data Structures', 'CSC202', 'Advanced data structures and algorithms', 40, 2, TRUE, DATE '2024-09-01', DATE '2024-12-15', TIMESTAMP '2023-09-02', TIMESTAMP '2024-09-02'),
('Database Systems', 'CSC303', 'Introduction to database design and management', 45, 3, TRUE, DATE '2024-09-01', DATE '2024-12-15', TIMESTAMP '2023-09-03', TIMESTAMP '2024-09-03'),
('Web Development', 'CSC404', 'Full-stack web development fundamentals', 35, 4, TRUE, DATE '2024-09-01', DATE '2024-12-15', TIMESTAMP '2023-09-04', TIMESTAMP '2024-09-04'),
('Operating Systems', 'CSC505', 'Principles of operating systems', 30, 5, TRUE, DATE '2024-09-01', DATE '2024-12-15', TIMESTAMP '2023-09-05', TIMESTAMP '2024-09-05'),
('Computer Networks', 'CSC606', 'Network architecture and protocols', 40, 6, TRUE, DATE '2024-09-01', DATE '2024-12-15', TIMESTAMP '2023-09-06', TIMESTAMP '2024-09-06'),
('Software Engineering', 'CSC707', 'Software development methodologies', 35, 7, TRUE, DATE '2024-09-01', DATE '2024-12-15', TIMESTAMP '2023-09-07', TIMESTAMP '2024-09-07'),
('Artificial Intelligence', 'CSC808', 'Introduction to AI and machine learning', 30, 8, TRUE, DATE '2024-09-01', DATE '2024-12-15', TIMESTAMP '2023-09-08', TIMESTAMP '2024-09-08'),
('Cybersecurity', 'CSC909', 'Principles of information security', 25, 9, TRUE, DATE '2024-09-01', DATE '2024-12-15', TIMESTAMP '2023-09-09', TIMESTAMP '2024-09-09'),
('Cloud Computing', 'CSC1010', 'Cloud architecture and services', 30, 10, TRUE, DATE '2024-09-01', DATE '2024-12-15', TIMESTAMP '2023-09-10', TIMESTAMP '2024-09-10');

-- Enrollments
INSERT INTO "Enrollment" (student_id, course_id, status, enrollment_date) VALUES
(1, 1, 'enrolled', DATE '2023-09-02'),
(1, 2, 'enrolled', DATE '2023-09-02'),
(2, 1, 'enrolled', DATE '2023-09-03'),
(2, 3, 'enrolled', DATE '2023-09-03'),
(3, 2, 'enrolled', DATE '2023-09-04'),
(3, 4, 'enrolled', DATE '2023-09-04'),
(4, 3, 'enrolled', DATE '2023-09-05'),
(4, 5, 'enrolled', DATE '2023-09-05'),
(5, 4, 'enrolled', DATE '2023-09-06'),
(5, 6, 'enrolled', DATE '2023-09-06'),
(6, 5, 'enrolled', DATE '2023-09-07'),
(6, 7, 'enrolled', DATE '2023-09-07'),
(7, 6, 'enrolled', DATE '2023-09-08'),
(7, 8, 'enrolled', DATE '2023-09-08'),
(8, 7, 'enrolled', DATE '2023-09-09'),
(8, 9, 'enrolled', DATE '2023-09-09'),
(9, 8, 'enrolled', DATE '2023-09-10'),
(9, 10, 'enrolled', DATE '2023-09-10'),
(10, 9, 'enrolled', DATE '2023-09-11'),
(10, 1, 'enrolled', DATE '2023-09-11');

-- Exams
INSERT INTO "Exam" (course_id, exam_name, exam_description, start_date, end_date, created_at, updated_at) VALUES
(1, 'Midterm Exam 1', 'Covers chapters 1-5 of Intro to CS', TIMESTAMP '2024-10-10', TIMESTAMP '2024-10-10', TIMESTAMP '2024-09-01', TIMESTAMP '2024-10-01'),
(1, 'Final Exam', 'Comprehensive final exam for Intro to CS', TIMESTAMP '2024-12-10', TIMESTAMP '2024-12-10', TIMESTAMP '2024-11-01', TIMESTAMP '2024-12-01'),
(2, 'Data Structures Midterm', 'Covers arrays, linked lists, and stacks', TIMESTAMP '2024-10-15', TIMESTAMP '2024-10-15', TIMESTAMP '2024-09-05', TIMESTAMP '2024-10-05'),
(2, 'Data Structures Final', 'Comprehensive data structures exam', TIMESTAMP '2024-12-15', TIMESTAMP '2024-12-15', TIMESTAMP '2024-11-05', TIMESTAMP '2024-12-05'),
(3, 'Database Midterm', 'Covers ER modeling and SQL basics', TIMESTAMP '2024-10-20', TIMESTAMP '2024-10-20', TIMESTAMP '2024-09-10', TIMESTAMP '2024-10-10'),
(3, 'Database Final', 'Advanced SQL and database design', TIMESTAMP '2024-12-20', TIMESTAMP '2024-12-20', TIMESTAMP '2024-11-10', TIMESTAMP '2024-12-10'),
(4, 'Web Dev Midterm', 'HTML, CSS, and JavaScript basics', TIMESTAMP '2024-10-25', TIMESTAMP '2024-10-25', TIMESTAMP '2024-09-15', TIMESTAMP '2024-10-15'),
(4, 'Web Dev Final', 'Full-stack development concepts', TIMESTAMP '2024-12-25', TIMESTAMP '2024-12-25', TIMESTAMP '2024-11-15', TIMESTAMP '2024-12-15'),
(5, 'OS Midterm', 'Process management and scheduling', TIMESTAMP '2024-10-30', TIMESTAMP '2024-10-30', TIMESTAMP '2024-09-20', TIMESTAMP '2024-10-20'),
(5, 'OS Final', 'Memory management and file systems', TIMESTAMP '2024-12-30', TIMESTAMP '2024-12-30', TIMESTAMP '2024-11-20', TIMESTAMP '2024-12-20');

-- Questions
INSERT INTO "Question" (exam_id, question_text, created_at, updated_at) VALUES
(1, 'What is a variable in programming?', TIMESTAMP '2024-09-05', TIMESTAMP '2024-09-06'),
(1, 'Explain the concept of loops in programming.', TIMESTAMP '2024-09-05', TIMESTAMP '2024-09-06'),
(1, 'What is object-oriented programming?', TIMESTAMP '2024-09-05', TIMESTAMP '2024-09-06'),
(2, 'What are the main data types in Python?', TIMESTAMP '2024-09-10', TIMESTAMP '2024-09-11'),
(2, 'Explain the difference between a list and a tuple.', TIMESTAMP '2024-09-10', TIMESTAMP '2024-09-11'),
(3, 'What is the time complexity of binary search?', TIMESTAMP '2024-09-15', TIMESTAMP '2024-09-16'),
(3, 'Explain how a hash table works.', TIMESTAMP '2024-09-15', TIMESTAMP '2024-09-16'),
(4, 'What is normalization in databases?', TIMESTAMP '2024-09-20', TIMESTAMP '2024-09-21'),
(4, 'Explain the ACID properties of transactions.', TIMESTAMP '2024-09-20', TIMESTAMP '2024-09-21'),
(5, 'What is the box model in CSS?', TIMESTAMP '2024-09-25', TIMESTAMP '2024-09-26');

-- Answers
INSERT INTO "Answer" (answer_text, question_id, created_at, updated_at) VALUES
('A variable stores data values', 1, TIMESTAMP '2024-09-07', TIMESTAMP '2024-09-08'),
('Loops are used to repeat a block of code multiple times', 2, TIMESTAMP '2024-09-07', TIMESTAMP '2024-09-08'),
('OOP is a programming paradigm based on objects and classes', 3, TIMESTAMP '2024-09-07', TIMESTAMP '2024-09-08'),
('Integer, float, string, boolean, list, tuple, dictionary', 4, TIMESTAMP '2024-09-12', TIMESTAMP '2024-09-13'),
('Lists are mutable while tuples are immutable', 5, TIMESTAMP '2024-09-12', TIMESTAMP '2024-09-13'),
('O(log n)', 6, TIMESTAMP '2024-09-17', TIMESTAMP '2024-09-18'),
('A hash table uses a hash function to map keys to values', 7, TIMESTAMP '2024-09-17', TIMESTAMP '2024-09-18'),
('Normalization is the process of organizing data to reduce redundancy', 8, TIMESTAMP '2024-09-22', TIMESTAMP '2024-09-23'),
('Atomicity, Consistency, Isolation, Durability', 9, TIMESTAMP '2024-09-22', TIMESTAMP '2024-09-23'),
('The box model describes how elements are rendered with padding, border, and margin', 10, TIMESTAMP '2024-09-27', TIMESTAMP '2024-09-28');

-- Student Answers
INSERT INTO "Student_Answer" (student_id, question_id, answer_text, second_attempt_answer, answer_grade, second_attempt_grade, answer_stage) VALUES
(1, 1, 'A variable is a data holder', 'A variable stores data values', 'B', 'A', 1),
(1, 2, 'Loops repeat code', 'Loops are used to repeat a block of code multiple times', 'B', 'A', 1),
(2, 1, 'A variable stores information', 'A variable stores data values', 'B', 'A', 1),
(2, 3, 'OOP uses objects', 'OOP is a programming paradigm based on objects and classes', 'B', 'A', 1),
(3, 4, 'int, float, str, bool', 'Integer, float, string, boolean, list, tuple, dictionary', 'B', 'A', 1),
(3, 5, 'Lists can change, tuples cannot', 'Lists are mutable while tuples are immutable', 'A', 'A', 1),
(4, 6, 'logarithmic time', 'O(log n)', 'A', 'A', 1),
(4, 7, 'Hash tables use keys and values', 'A hash table uses a hash function to map keys to values', 'B', 'A', 1),
(5, 8, 'Making data more efficient', 'Normalization is the process of organizing data to reduce redundancy', 'B', 'A', 1),
(5, 9, 'ACID stands for database properties', 'Atomicity, Consistency, Isolation, Durability', 'B', 'A', 1);

-- AI Assessments
INSERT INTO "AI_Assessment" (assessment_text, student_answer_id, grade) VALUES
('Good understanding of variables, but could be more precise', 1, 'B'),
('Basic understanding of loops, needs more detail', 2, 'B'),
('Good start, but needs to expand on the concept', 3, 'B'),
('Accurate but incomplete list of data types', 4, 'B'),
('Excellent understanding of the difference between lists and tuples', 5, 'A'),
('Perfect understanding of time complexity', 6, 'A'),
('Good start, but needs to explain the hash function concept', 7, 'B'),
('Basic understanding, needs to explain the normalization process', 8, 'B'),
('Good attempt, but should list all ACID properties', 9, 'B'),
('Excellent understanding of the CSS box model', 10, 'A'); 