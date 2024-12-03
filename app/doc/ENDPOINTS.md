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

- **Description**: Create an answer for a question

- **Request Body**:
    ```json
    {
    }
    ```

- **Response Body**:
    ```json
    {
    }
    ```

## course

### GET `api/v1/get_active_courses_for_teacher/<int:teacher_id>`

- **Description**: Get active courses for a teacher

- **Request Body**:
    ```json
    {
    }
    ```

### CREATE `api/v1/create_course/<int:teacher_id>`

- **Description**: Create a course

- **Request Body**:
    ```json
    {
    }
    ```

### PUT `api/v1/update_course/<int:course_id>`

- **Description**: Update a course

- **Request Body**:
    ```json
    {
    }
    ```

### PUT `api/v1/change_course_status/<int:course_id>`

- **Description**: Change the status of a course

- **Request Body**:
    ```json
    {
    }
    ```

### GET `api/v1/get_active_courses_for_student/<int:student_id>`

- **Description**: Get active courses for a student

- **Request Body**:
    ```json
    {
    }
    ```


## enrollment

### PUT `api/v1/change_enrollment_status_for_student/<int:student_id>/<int:course_id>/<string:status>`

- **Description**: Change the enrollment status for a student

- **Request Body**:
    ```json
    {
    }
    ```

### CREATE `api/v1/create_enrollment/<int:student_id>/<int:course_id>`

- **Description**: Create an enrollment for a student

- **Request Body**:
    ```json
    {
    }
    ```




## exam

### GET `api/v1/get_exams_for_teacher/<int:teacher_id>`

- **Description**: Get exams for a teacher

- **Request Body**:
    ```json
    {
    }
    ```

### GET `api/v1/get_exams_for_course/<int:course_id>`

- **Description**: Get exams for a course

- **Request Body**:
    ```json
    {
    }
    ```

### CREATE `api/v1/create_exam/<int:course_id>`

- **Description**: Create an exam

- **Request Body**:
    ```json
    {
    }
    ```

### GET `api/v1/get_exam_submission_number/<int:exam_id>/<int:student_id>`

- **Description**: Get the number of submissions for an exam

- **Request Body**:
    ```json
    {
    }
    ```

### GET `api/v1/get_exams_for_student/<int:student_id>`

- **Description**: Get exams for a student

- **Request Body**:
    ```json
    {
    }
    ```

## question

### CREATE `api/v1/create_question/<int:exam_id>`

- **Description**: Create a question for an exam

- **Request Body**:
    ```json
    {
    }
    ```

### GET `api/v1/get_questions_for_exam/<int:exam_id>`

- **Description**: Get questions for an exam

- **Request Body**:
    ```json
    {
    }
    ```


## student

### GET `api/v1/search_for_students/<str:search_query>`

- **Description**: Search for students

- **Request Body**:
    ```json
    {
    }
    ```

### GET `api/v1/get_students_for_course/<int:course_id>`

- **Description**: Get students for a course

- **Request Body**:
    ```json
    {
    }
    ```

## studentAnswer

### GET `api/v1/get_student_answers_for_student/<int:student_id>/<int:question_id>`

- **Description**: Get student answers for a student

- **Request Body**:
    ```json
    {
    }
    ```

### CREATE `api/v1/create_student_answer/<int:student_id>/<int:question_id>`

- **Description**: Create a student answer

- **Request Body**:
    ```json
    {
    }
    ```



## teacher

### GET `api/v1/teacher_by_id/<int:teacher_id>`

- **Description**: Get a teacher by their ID

- **Request Body**:
  ```json
  {
    "teacher": {
      "email": "Tsmith1@brockport.edu",
  }
  ```
