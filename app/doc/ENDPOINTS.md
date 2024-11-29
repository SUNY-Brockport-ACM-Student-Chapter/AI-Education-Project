# API Endpoints

## Table of Contents
1. [ai assesment](#ai-assesment)

    1. Teacher
        - [GET `api/v1/get_ai_assesment_for_studentAnswer/<int:studentAnswer_id>`](#get-apiv1get_ai_assesment_for_studentAnswerintstudentAnswer_id)

    2. Student


2. [answer](#answer)

    1. Teacher

    2. Student


3. [course](#course)

    1. Teacher
        - [GET `api/v1/get_active_courses_for_teacher/<int:teacher_id>`](#get-apiv1get_active_courses_for_teacherintteacher_id)
        - [CREATE `api/v1/create_course/<int:teacher_id>`](#create-apiv1create_courseintteacher_id)
        - [PUT `api/v1/update_course/<int:course_id>`](#put-apiv1update_courseintcourse_id)
        - [PUT `api/v1/change_course_status/<int:course_id>`](#put-apiv1change_course_statusintcourse_id)
        - [PUT `api/v1/update_exam/<int:exam_id>`](#put-apiv1update_examintexam_id)

    2. Student


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




6. [question](#question)
    1. Teacher
        - [CREATE `api/v1/create_question/<int:exam_id>`](#create-apiv1create_questionintexam_id)
        - [GET `api/v1/get_questions_for_exam/<int:exam_id>`](#get-apiv1get_questions_for_examintexam_id)

    2. Student




7. [student](#student)
    1. Teacher
        - [GET `api/v1/search_for_students/<str:search_query>`](#get-apiv1search_for_studentsstrsearch_query)
        - [GET `api/v1/get_students_for_course/<int:course_id>`](#get-apiv1get_students_for_courseintcourse_id)

    2. Student



8. [studentAnswer](#studentAnswer)
    1. Teacher
        - [GET `api/v1/get_student_answers_for_student/<int:student_id>/<int:question_id>`](#get-apiv1get_student_answers_for_studentintstudent_idintquestion_id)

    2. Student




9. [teacher](#teacher)
    1. Teacher
        - [GET `api/v1/teacher_by_id/<int:teacher_id>`](#get-apiv1teacher_by_idintteacher_id)

    2. Student






## ai assesment

### GET `api/v1/get_ai_assesment_for_studentAnswer/<int:studentAnswer_id>`

- **Description**: Get AI assesment for a student answer

- **Request Body**:
    ```json
    {
        "ai_assesment": {
            "assesment": "The student's answer is correct",
            "assesment_id": 1
        }
    }
    ```

## answer

## course

### GET `api/v1/get_active_courses_for_teacher/<int:teacher_id>`

### CREATE `api/v1/create_course/<int:teacher_id>`

### PUT `api/v1/update_course/<int:course_id>`

### PUT `api/v1/change_course_status/<int:course_id>`

### PUT `api/v1/update_exam/<int:exam_id>`

## enrollment

## exam

## question


## student

## studentAnswer


## teacher

### GET `/api/v1/teacher_dashboard_data/<int:teacher_id>`

- **Description**: Get dashboard data for a specific teacher by teacher_id

- **Request Body**:
  ```json 
  {
  "dashboard_data": {
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
    ],
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
    ],
    "teacher": {
      "email": "Tsmith1@brockport.edu",
      "first_name": "Tom",
      "last_name": "Smith",
      "teacher_id": 1,
      "user_name": "Tsmith1"
    }
    }
  }
  ```

