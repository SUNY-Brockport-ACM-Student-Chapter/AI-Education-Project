-- Mock Data Generation
-- Students
INSERT INTO Student (user_name, first_name, last_name, email, clerk_user_id, is_active, last_login, created_at, updated_at) VALUES
('Jdoe1', 'John', 'Doe', 'jdoe1@brockport.edu', 'Abc123hashedpassword', TRUE, '2024-09-15', '2023-09-01', '2023-08-15'),
('Sjohnson2', 'Sarah', 'Johnson', 'sjohnson2@brockport.edu', 'Def456hashedpassword', TRUE, '2024-09-16', '2023-09-02', '2023-08-16'),
('Mwilliams3', 'Michael', 'Williams', 'mwilliams3@brockport.edu', 'Ghi789hashedpassword', TRUE, '2024-09-17', '2023-09-03', '2023-08-17'),
('Emartinez4', 'Emily', 'Martinez', 'emartinez4@brockport.edu', 'Jkl012hashedpassword', TRUE, '2024-09-18', '2023-09-04', '2023-08-18'),
('Rgarcia5', 'Robert', 'Garcia', 'rgarcia5@brockport.edu', 'Mno345hashedpassword', TRUE, '2024-09-19', '2023-09-05', '2023-08-19'),
('Lbrown6', 'Lisa', 'Brown', 'lbrown6@brockport.edu', 'Pqr678hashedpassword', TRUE, '2024-09-20', '2023-09-06', '2023-08-20'),
('Dmiller7', 'David', 'Miller', 'dmiller7@brockport.edu', 'Stu901hashedpassword', TRUE, '2024-09-21', '2023-09-07', '2023-08-21'),
('Jdavis8', 'Jennifer', 'Davis', 'jdavis8@brockport.edu', 'Vwx234hashedpassword', TRUE, '2024-09-22', '2023-09-08', '2023-08-22'),
('Trodriguez9', 'Thomas', 'Rodriguez', 'trodriguez9@brockport.edu', 'Yza567hashedpassword', TRUE, '2024-09-23', '2023-09-09', '2023-08-23'),
('Mwilson10', 'Mary', 'Wilson', 'mwilson10@brockport.edu', 'Bcd890hashedpassword', TRUE, '2024-09-24', '2023-09-10', '2023-08-24');

-- Teachers
INSERT INTO Teacher (user_name, first_name, last_name, email, clerk_user_id, role, is_active, last_login, created_at, updated_at) VALUES
('Tsmith1', 'Tom', 'Smith', 'Tsmith1@brockport.edu', 'Abc123hashedpassword', 'teacher', TRUE, '2024-09-17', '2023-07-20', '2024-07-22'),
('Janderson2', 'Jane', 'Anderson', 'janderson2@brockport.edu', 'Def456hashedpassword', 'teacher', TRUE, '2024-09-18', '2023-07-21', '2024-07-23'),
('Rthomas3', 'Richard', 'Thomas', 'rthomas3@brockport.edu', 'Ghi789hashedpassword', 'teacher', TRUE, '2024-09-19', '2023-07-22', '2024-07-24'),
('Lmoore4', 'Laura', 'Moore', 'lmoore4@brockport.edu', 'Jkl012hashedpassword', 'teacher', TRUE, '2024-09-20', '2023-07-23', '2024-07-25'),
('Staylor5', 'Steven', 'Taylor', 'staylor5@brockport.edu', 'Mno345hashedpassword', 'teacher', TRUE, '2024-09-21', '2023-07-24', '2024-07-26'),
('Awhite6', 'Amanda', 'White', 'awhite6@brockport.edu', 'Pqr678hashedpassword', 'teacher', TRUE, '2024-09-22', '2023-07-25', '2024-07-27'),
('Pjackson7', 'Paul', 'Jackson', 'pjackson7@brockport.edu', 'Stu901hashedpassword', 'teacher', TRUE, '2024-09-23', '2023-07-26', '2024-07-28'),
('Cmartin8', 'Catherine', 'Martin', 'cmartin8@brockport.edu', 'Vwx234hashedpassword', 'teacher', TRUE, '2024-09-24', '2023-07-27', '2024-07-29'),
('Dthompson9', 'Daniel', 'Thompson', 'dthompson9@brockport.edu', 'Yza567hashedpassword', 'teacher', TRUE, '2024-09-25', '2023-07-28', '2024-07-30'),
('Hclark10', 'Helen', 'Clark', 'hclark10@brockport.edu', 'Bcd890hashedpassword', 'teacher', TRUE, '2024-09-26', '2023-07-29', '2024-07-31');

-- Courses
INSERT INTO Course (course_name, course_code, course_description, capacity, teacher_id, is_active, start_date, end_date, created_at, updated_at) VALUES
('Intro to CS', 'CSC101', 'A beginner course on Computer Science fundamentals', 50, 1, TRUE, '2024-09-01', '2024-12-15', '2023-09-01', '2024-09-01'),
('Data Structures', 'CSC202', 'Advanced data structures and algorithms', 40, 2, TRUE, '2024-09-01', '2024-12-15', '2023-09-02', '2024-09-02'),
('Database Systems', 'CSC303', 'Introduction to database design and management', 45, 3, TRUE, '2024-09-01', '2024-12-15', '2023-09-03', '2024-09-03'),
('Web Development', 'CSC404', 'Full-stack web development fundamentals', 35, 4, TRUE, '2024-09-01', '2024-12-15', '2023-09-04', '2024-09-04'),
('Operating Systems', 'CSC505', 'Principles of operating systems', 30, 5, TRUE, '2024-09-01', '2024-12-15', '2023-09-05', '2024-09-05'),
('Computer Networks', 'CSC606', 'Network architecture and protocols', 40, 6, TRUE, '2024-09-01', '2024-12-15', '2023-09-06', '2024-09-06'),
('Software Engineering', 'CSC707', 'Software development methodologies', 35, 7, TRUE, '2024-09-01', '2024-12-15', '2023-09-07', '2024-09-07'),
('Artificial Intelligence', 'CSC808', 'Introduction to AI and machine learning', 30, 8, TRUE, '2024-09-01', '2024-12-15', '2023-09-08', '2024-09-08'),
('Cybersecurity', 'CSC909', 'Principles of information security', 25, 9, TRUE, '2024-09-01', '2024-12-15', '2023-09-09', '2024-09-09'),
('Cloud Computing', 'CSC1010', 'Cloud architecture and services', 30, 10, TRUE, '2024-09-01', '2024-12-15', '2023-09-10', '2024-09-10');

-- Enrollments
INSERT INTO Enrollment (student_id, course_id, status, enrollment_date) VALUES
(1, 1, 'enrolled', '2023-09-02'),
(1, 2, 'enrolled', '2023-09-02'),
(2, 1, 'enrolled', '2023-09-03'),
(2, 3, 'enrolled', '2023-09-03'),
(3, 2, 'enrolled', '2023-09-04'),
(3, 4, 'enrolled', '2023-09-04'),
(4, 3, 'enrolled', '2023-09-05'),
(4, 5, 'enrolled', '2023-09-05'),
(5, 4, 'enrolled', '2023-09-06'),
(5, 6, 'enrolled', '2023-09-06'),
(6, 5, 'enrolled', '2023-09-07'),
(6, 7, 'enrolled', '2023-09-07'),
(7, 6, 'enrolled', '2023-09-08'),
(7, 8, 'enrolled', '2023-09-08'),
(8, 7, 'enrolled', '2023-09-09'),
(8, 9, 'enrolled', '2023-09-09'),
(9, 8, 'enrolled', '2023-09-10'),
(9, 10, 'enrolled', '2023-09-10'),
(10, 9, 'enrolled', '2023-09-11'),
(10, 1, 'enrolled', '2023-09-11');

-- Exams
INSERT INTO Exam (course_id, exam_name, exam_description, start_date, end_date, created_at, updated_at) VALUES
(1, 'Midterm Exam 1', 'Covers chapters 1-5 of Intro to CS', '2024-10-10', '2024-10-10', '2024-09-01', '2024-10-01'),
(1, 'Final Exam', 'Comprehensive final exam for Intro to CS', '2024-12-10', '2024-12-10', '2024-11-01', '2024-12-01'),
(2, 'Data Structures Midterm', 'Covers arrays, linked lists, and stacks', '2024-10-15', '2024-10-15', '2024-09-05', '2024-10-05'),
(2, 'Data Structures Final', 'Comprehensive data structures exam', '2024-12-15', '2024-12-15', '2024-11-05', '2024-12-05'),
(3, 'Database Midterm', 'Covers ER modeling and SQL basics', '2024-10-20', '2024-10-20', '2024-09-10', '2024-10-10'),
(3, 'Database Final', 'Advanced SQL and database design', '2024-12-20', '2024-12-20', '2024-11-10', '2024-12-10'),
(4, 'Web Dev Midterm', 'HTML, CSS, and JavaScript basics', '2024-10-25', '2024-10-25', '2024-09-15', '2024-10-15'),
(4, 'Web Dev Final', 'Full-stack development concepts', '2024-12-25', '2024-12-25', '2024-11-15', '2024-12-15'),
(5, 'OS Midterm', 'Process management and scheduling', '2024-10-30', '2024-10-30', '2024-09-20', '2024-10-20'),
(5, 'OS Final', 'Memory management and file systems', '2024-12-30', '2024-12-30', '2024-11-20', '2024-12-20');

-- Questions
INSERT INTO Question (exam_id, question_text, created_at, updated_at) VALUES
(1, 'What is a variable in programming?', '2024-09-05', '2024-09-06'),
(1, 'Explain the concept of loops in programming.', '2024-09-05', '2024-09-06'),
(1, 'What is object-oriented programming?', '2024-09-05', '2024-09-06'),
(2, 'What are the main data types in Python?', '2024-09-10', '2024-09-11'),
(2, 'Explain the difference between a list and a tuple.', '2024-09-10', '2024-09-11'),
(3, 'What is the time complexity of binary search?', '2024-09-15', '2024-09-16'),
(3, 'Explain how a hash table works.', '2024-09-15', '2024-09-16'),
(4, 'What is normalization in databases?', '2024-09-20', '2024-09-21'),
(4, 'Explain the ACID properties of transactions.', '2024-09-20', '2024-09-21'),
(5, 'What is the box model in CSS?', '2024-09-25', '2024-09-26');

-- Answers
INSERT INTO Answer (answer_text, question_id, created_at, updated_at) VALUES
('A variable stores data values', 1, '2024-09-07', '2024-09-08'),
('Loops are used to repeat a block of code multiple times', 2, '2024-09-07', '2024-09-08'),
('OOP is a programming paradigm based on objects and classes', 3, '2024-09-07', '2024-09-08'),
('Integer, float, string, boolean, list, tuple, dictionary', 4, '2024-09-12', '2024-09-13'),
('Lists are mutable while tuples are immutable', 5, '2024-09-12', '2024-09-13'),
('O(log n)', 6, '2024-09-17', '2024-09-18'),
('A hash table uses a hash function to map keys to values', 7, '2024-09-17', '2024-09-18'),
('Normalization is the process of organizing data to reduce redundancy', 8, '2024-09-22', '2024-09-23'),
('Atomicity, Consistency, Isolation, Durability', 9, '2024-09-22', '2024-09-23'),
('The box model describes how elements are rendered with padding, border, and margin', 10, '2024-09-27', '2024-09-28');

-- Student Answers
INSERT INTO Student_Answer (student_id, question_id, answer_text, second_attempt_answer, answer_grade, second_attempt_grade, answer_stage) VALUES
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
INSERT INTO AI_Assessment (assessment_text, student_answer_id, grade) VALUES
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