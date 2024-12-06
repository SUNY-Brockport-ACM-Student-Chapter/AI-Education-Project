# API Endpoints

## Table of Contents
1. [ai assesment](#ai-assesment)

    1. Teacher
        - [GET `api/v1/get_ai_assesment_for_studentAnswer/<int:studentAnswer_id>`](#get-apiv1get_ai_assesment_for_studentAnswerintstudentAnswer_id)

    2. Student


2. [answer](#answer)

    1. Teacher
        - [CREATE `api/v1/create_answer/<int:question_id>`](#create-apiv1create_answerintquestion_id)

    2. Student


3. [course](#course)

    1. Teacher
        - [GET `api/v1/get_active_courses_for_teacher/<int:teacher_id>`](#get-apiv1get_active_courses_for_teacherintteacher_id)
        - [CREATE `api/v1/create_course/<int:teacher_id>`](#create-apiv1create_courseintteacher_id)
        - [PUT `api/v1/update_course/<int:course_id>`](#put-apiv1update_courseintcourse_id)
        - [PUT `api/v1/change_course_status/<int:course_id>`](#put-apiv1change_course_statusintcourse_id)
        - [PUT `api/v1/update_exam/<int:exam_id>`](#put-apiv1update_examintexam_id)

    2. Student

        - [GET `api/v1/get_active_courses_for_student/<int:student_id>`](#get-apiv1get_active_courses_for_studentintstudent_id)


4. [enrollment](#enrollment)
    1. Teacher
        - [PUT `api/v1/change_enrollment_status_for_student/<int:student_id>/<int:course_id>`](#put-apiv1change_enrollment_status_for_studentintstudent_idintcourse_id)
        - [CREATE `api/v1/create_enrollment/<int:student_id>/<int:course_id>`](#create-apiv1create_enrollmentintstudent_idintcourse_id)

    2. Student


5. [exam](#exam)
    1. Teacher
        - [GET `api/v1/get_exams_for_teacher/<int:teacher_id>`](#get-apiv1get_exams_for_teacherintteacher_id)
        - [GET `api/v1/get_exams_for_course/<int:course_id>`](#get-apiv1get_exams_for_courseintcourse_id)
        - [CREATE `api/v1/create_exam/<int:course_id>`](#create-apiv1create_examintcourse_id)
        - [GET `api/v1/get_exam_submission_number/<int:exam_id>`](#get-apiv1get_exam_submission_numberintexam_id)

    2. Student
        - [GET `api/v1/get_exams_for_student/<int:student_id>`](#get-apiv1get_exams_for_studentintstudent_id)
        - [GET `api/v1/get_exams_for_course/<int:course_id>`](#get-apiv1get_exams_for_courseintcourse_id)
        - [GET `api/v1/get_exam_submission_number/<int:exam_id>`](#get-apiv1get_exam_submission_numberintexam_id)

6. [question](#question)
    1. Teacher
        - [CREATE `api/v1/create_question/<int:exam_id>`](#create-apiv1create_questionintexam_id)
        - [GET `api/v1/get_questions_for_exam/<int:exam_id>`](#get-apiv1get_questions_for_examintexam_id)

    2. Student
        - [GET `api/v1/get_questions_for_exam/<int:exam_id>`](#get-apiv1get_questions_for_examintexam_id)



7. [student](#student)
    1. Teacher
        - [GET `api/v1/search_for_students/<str:search_query>`](#get-apiv1search_for_studentsstrsearch_query)
        - [GET `api/v1/get_students_for_course/<int:course_id>`](#get-apiv1get_students_for_courseintcourse_id)

    2. Student



8. [studentAnswer](#studentAnswer)
    1. Teacher
        - [GET `api/v1/get_student_answers_for_student/<int:student_id>/<int:question_id>`](#get-apiv1get_student_answers_for_studentintstudent_idintquestion_id)

    2. Student
        - [CREATE `api/v1/create_student_answer/<int:student_id>/<int:question_id>`](#create-apiv1create_student_answerintstudent_idintquestion_id)



9. [teacher](#teacher)
    1. Teacher
        - [GET `api/v1/teacher_by_id/<int:teacher_id>`](#get-apiv1teacher_by_idintteacher_id)

    2. Student






## ai assesment

### GET `api/v1/get_ai_assesment_for_studentAnswer/<int:studentAnswer_id>`

- **Example**:
    ```
    api/v1/get_ai_assesment_for_studentAnswer/1
    ```

- **Description**: Get AI assesment for a student answer

- **Response Body**:
    ```json
    {
        "Id": 1,
        "assessment_text": "Very good answer",
        "grade": "S",
        "student_answer_id": 1
    }
    ```

## answer

### CREATE `api/v1/create_answer/<int:question_id>`

- **Example**:
    ```
    api/v1/create_answer/1
    ```

- **Description**: Create an answer for a question

- **Request Body**:
    ```json
    {
        "answer_text": "Hello world"
    }
    ```

- **Response Body**:
    ```json
    {
        "answer": {
            "answer_id": 9,
            "answer_text": "Big Byt bur",
            "question_id": 1
        },
        "message": "Answer created successfully"
    }
    ```

## course

### GET `api/v1/get_active_courses_for_teacher/<int:teacher_id>`

- **Example**:
    ```
    api/v1/get_active_courses_for_teacher/1
    ```

- **Description**: Get active courses for a teacher

- **Response Body**:
    ```json
    {
        "courses": [
                {
                    "capacity": 50,
                    "course_code": "1",
                    "course_description": "A beginner course on CS",
                    "course_name": "Intro to CS",
                    "end_date": "2024-11-22T00:00:00",
                    "is_active": true,
                "start_date": "2024-11-22T00:00:00",
                "teacher_id": 1
            }
        ]   
    }
    ```

### CREATE `api/v1/create_course/<int:teacher_id>`

- **Example**:
    ```
    api/v1/create_course/1
    ```

- **Description**: Create a course

- **Request Body**:
    ```json
    {
        "course_name": "intro to relations",
        "course_code": "1",
        "course_description": "Interpersonal relations",
        "capacity": "13",
        "start_date": "2024-11-22 00:00:00",
        "end_date": "2024-11-22 00:00:00"
    }
    ```

- **Response Body**:
    ```json
    {
        "course": {
            "capacity": 13,
            "course_code": "1",
            "course_description": "Interpersonal relations",
            "course_name": "intro to relations",
            "end_date": "2024-11-22T00:00:00",
            "is_active": true,
            "start_date": "2024-11-22T00:00:00",
            "teacher_id": 1
        },
        "message": "Course created successfully"
    }
    ```

### PUT `api/v1/update_course/<int:course_id>`

- **Example**:
    ```
    api/v1/update_course/1
    ```

- **Description**: Update a course

- **Request Body**:
    ```json
    {
        "course_code": "4",
        "course_description": "A beginner course on js"
    }
    ```

- **Response Body**:
    ```json
    {
        "course": {
            "capacity": 50,
            "course_code": "4",
            "course_description": "A beginner course on js",
            "course_name": "Intro to CS",
            "end_date": "2024-11-22T00:00:00",
            "is_active": true,
            "start_date": "2024-11-22T00:00:00",
            "teacher_id": 1
        },
        "message": "Course updated successfully"
    }
    ```


### PUT `api/v1/change_course_status/<int:course_id>`

- **Example**:
    ```
    api/v1/change_course_status/1
    ```

- **Description**: Change the status of a course

- **Response Body**:
    ```json
    {
        "course": {
            "capacity": 50,
            "course_code": "1",
            "course_description": "A beginner course on CS",
            "course_name": "Intro to CS",
            "end_date": "2024-11-22T00:00:00",
            "is_active": true,
            "start_date": "2024-11-22T00:00:00",
            "teacher_id": 1
        },
        "message": "Course status changed successfully"
    }
    ```

### GET `api/v1/get_active_courses_for_student/<int:student_id>`

- **Example**:
    ```
    api/v1/get_active_courses_for_student/1
    ```

- **Description**: Get active courses for a student

- **Response Body**:
    ```json
    {
        "courses": [
            {
                "capacity": 50,
                "course_code": "4",
                "course_description": "A beginner course on js",
                "course_name": "Intro to CS",
                "end_date": "2024-11-22T00:00:00",
                "is_active": true,
                "start_date": "2024-11-22T00:00:00",
                "teacher_id": 1
            }
        ]
    }
    ```


## enrollment

### PUT `api/v1/change_enrollment_status_for_student/<int:student_id>/<int:course_id>`

- **Description**: Change the enrollment status for a student

- **Example**:
    ```
    api/v1/change_enrollment_status_for_student/1/1
    ```

- **Status**:
    - "enrolled"    # default
    - "cancelled"   # cancels the enrollment
    - "padding"     # puts the enrollment on pending list

- **Request Body**:
    ```json
    {
        "status": "cancelled"
    }
    ```

- **Response Body**:
    ```json
    {
        "enrollment": {
            "course_id": 1,
            "enrollment_date": "2023-09-02T00:00:00",
            "enrollment_id": 1,
            "status": "cancelled",
            "student_id": 1
        },
        "message": "Enrollment status changed successfully"
    }
    ```


### CREATE `api/v1/create_enrollment/<int:student_id>/<int:course_id>`

- **Example**:
    ```
    api/v1/create_enrollment/1/1
    ```

- **Description**: Create an enrollment for a student

- **Response Body**:
    ```json
    {
        "enrollment": {
                "course_id": 1,
                "enrollment_date": "2024-12-05T21:53:51",
                "enrollment_id": 3,
                "status": "enrolled",
            "student_id": 1
        },
        "message": "Enrollment created successfully"
    }
    ```


## exam

### GET `api/v1/get_exams_for_teacher/<int:teacher_id>`

- **Example**:
    ```
    api/v1/get_exams_for_teacher/1
    ```

- **Description**: Get exams for a teacher

- **Response Body**:
    ```json
    {
        "exams": [
            {
                "course_id": 1,
                "description": "Covers chapters 1-5 of intro to cs",
                "end_date": "2024-10-10T00:00:00",
                "exam_id": 1,
                "max_attempts": 2,
                "name": "Midterm exam 1",
                "start_date": "2024-10-10T00:00:00"
            }
        ]
    }
    ```

### GET `api/v1/get_exams_for_course/<int:course_id>`

- **Example**:
    ```
    api/v1/get_exams_for_course/1
    ```

- **Description**: Get exams for a course

- **Response Body**:
    ```json
    {
        "exams": [
            {
                "course_id": 1,
                "description": "Covers chapters 1-5 of intro to cs",
                "end_date": "2024-10-10T00:00:00",
                "exam_id": 1,
                "max_attempts": 2,
                "name": "Midterm exam 1",
                "start_date": "2024-10-10T00:00:00"
            }
        ]
    }
    ```

### CREATE `api/v1/create_exam_for_course/<int:course_id>`

- **Example**:
    ```
    api/v1/create_exam_for_course/1
    ```

- **Description**: Create an exam for a course

- **Request Body**:
    ```json
    {
        "exam_name": "exam 4",
        "exam_description": "Big Exam",
        "max_attempt": "2",
        "start_date": "2024-10-10 00:00:00",
        "end_date": "2024-10-10 00:00:00"
    }
    ```

- **Response Body**:
    ```json
    {
        "exam": {
            "course_id": 1,
            "description": "Big Exam",
            "end_date": "2024-10-10T00:00:00",
            "exam_id": 2,
            "max_attempts": 2,
            "name": "exam 4",
            "start_date": "2024-10-10T00:00:00"
        },
        "message": "Exam created successfully"
    }
    ```

### GET `api/v1/get_student_exam_submission_stage/<int:exam_id>/<int:student_id>`

- **Example**:
    ```
    api/v1/get_student_exam_submission_stage/1/1
    ```

- **Description**: Get the submission stage for a student in an exam

- **Response Body**:
    ```json
    {
        "stage": 1
    }
    ```

### GET `api/v1/get_exams_for_student/<int:student_id>`

- **Example**:
    ```
    api/v1/get_exams_for_student/1
    ```

- **Description**: Get exams for a student

- **Response Body**:
    ```json
    {
        "exams": [
            {
                "course_id": 1,
                "description": "Covers chapters 1-5 of intro to cs",
                "end_date": "2024-10-10T00:00:00",
                "exam_id": 1,
                "max_attempts": 2,
                "name": "Midterm exam 1",
                "start_date": "2024-10-10T00:00:00"
            },
            {
                "course_id": 1,
                "description": "Big Exam",
                "end_date": "2024-10-10T00:00:00",
                "exam_id": 2,
                "max_attempts": 2,
                "name": "exam 4",
                "start_date": "2024-10-10T00:00:00"
            }
        ],
        "message": "Exams fetched successfully"
    }
    ```



## question

### CREATE `api/v1/create_question/<int:exam_id>`

- **Example**:
    ```
    api/v1/create_question/1
    ```

- **Description**: Create a question for an exam

- **Request Body**:
    ```json
    {
        "question_text": "How old is ryan?"
    }
    ```

- **Response Body**:
    ```json
    {
        "message": "Question created successfully",
        "question": {
            "exam_id": 1,
            "question_id": 2,
            "question_text": "How old is ryan?"
        }
    }
    ```

### GET `api/v1/get_questions_for_exam/<int:exam_id>`

- **Example**:
    ```
    api/v1/get_questions_for_exam/1
    ```

- **Description**: Get questions for an exam

- **Response Body**:
    ```json
    {
        "questions": [
            {
                "exam_id": 1,
                "question_id": 1,
                "question_text": "What is a variable in programming"
            },
            {
                "exam_id": 1,
                "question_id": 2,
                "question_text": "How old is ryan?"
            }
        ]
    }
    ```


## student

### GET `api/v1/search_for_students`

- **Example**:
    ```
    api/v1/search_for_students
    ```

- **Description**: Search for students

- **Request Body**:
    ```json
    {
        "first_name": "bendo"
    }
    ```

- **Response Body**:
    ```json
    {
        "students": [
            {
                "email": "pilse",
                "first_name": "bendo",
                "last_name": "smite",
                "student_id": 3,
                "user_name": "runner12"
            }
        ]
    }
    ```

### GET `api/v1/get_students_for_course/<int:course_id>`

- **Example**:
    ```
    api/v1/get_students_for_course/1
    ```

- **Description**: Get students for a course

- **Response Body**:
    ```json
    {
        "students": [
            {
                "email": "jdoe1@brockport.edu",
                "first_name": "John",
                "last_name": "smith",
                "student_id": 1,
                "user_name": "Jdoe1"
            }
        ]
    }
    ```

## studentAnswer

### GET `api/v1/get_student_answers_for_student/<int:student_id>/<int:question_id>`

- **Example**:
    ```
    api/v1/get_student_answers_for_student/1/1
    ```

- **Description**: Get student answers for a student

- **Response Body**:
    ```json
    {
        "student_answers": [
            {
                "answer_grade": "S",
                "answer_stage": 1,
                "answer_text": "A variable is a data holder",
                "question_id": 1,
                "second_attempt_answer": "A variable is a data holder",
                "second_attempt_grade": "S",
                "student_answer_id": 1,
                "student_id": 1
            }
        ]
    }
    ```

### CREATE `api/v1/create_student_answer/<int:student_id>/<int:question_id>`

- **Example**:
    ```
    api/v1/create_student_answer/1/1
    ```

- **Description**: Create a student answer

- **Request Body**:
    ```json
    {
        "answer_text":"Ryan is Tall",
        "answer_grade":"N",
        "answer_stage":"1"
    }
    ```

- **Response Body**:
    ```json
    {
        "student_answer": {
            "answer_grade": "N",
            "answer_stage": 1,
            "answer_text": "Ryan is Tall",
            "question_id": 1,
            "second_attempt_answer": "Ryan is Tall",
            "second_attempt_grade": "N",
            "student_answer_id": 2,
                "student_id": 1
        }
    }
    ```



## teacher

### GET `api/v1/get_teacher_by_id/<int:teacher_id>`

- **Example**:
    ```
    api/v1/get_teacher_by_id/1
    ```

- **Description**: Get a teacher by their ID

- **Response Body**:
    ```json
    {
        "teacher": {
            "email": "Tsmith1@brockport.edu",
            "first_name": "Tom",
            "last_name": "Smith",
            "teacher_id": 1,
            "user_name": "Tsmith1"
        }
    }
    ```