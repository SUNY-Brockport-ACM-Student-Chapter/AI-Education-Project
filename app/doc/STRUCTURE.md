## Project Structure

```
project_root/
├── run.py                  # Application entry point
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not in version control)
├── app/                    # Main application package
│   ├── __init__.py         # Application factory and initialization
│   ├── config.py           # Configuration settings
│   ├── database.py         # Database configuration
│   ├── models/             # Database models
│   │   ├── __init__.py
│   │   ├── student_model.py
│   │   ├── teacher_model.py
│   │   ├── course_model.py
│   │   ├── exam_model.py
│   │   ├── question_model.py
│   │   ├── answer_model.py
│   │   ├── studentAnswer_model.py
│   │   ├── enrollment_model.py
│   │   └── ai_assessment_model.py
│   ├── routes/             # API endpoints
│   │   ├── __init__.py
│   │   ├── main_routes.py
│   │   ├── user_routes.py
│   │   ├── student_routes.py
│   │   ├── teacher_routes.py
│   │   ├── course_routes.py
│   │   ├── exam_routes.py
│   │   ├── question_routes.py
│   │   ├── answer_routes.py
│   │   ├── studentAnswer_routes.py
│   │   ├── enrollment_routes.py
│   │   └── ai_assessment_routes.py
│   ├── services/           # Business logic
│   ├── repositories/       # Data access layer
│   ├── utils/              # Utility functions
│   ├── webhooks/           # Webhook handlers
│   ├── langchain/          # AI integration
│   │   ├── __init__.py
│   │   ├── chains.py
│   │   └── prompts.py
│   └── doc/                # Documentation
│       ├── SETUP.md
│       ├── STRUCTURE.md
│       ├── ENDPOINTS.md
│       └── Schema.sql
```
