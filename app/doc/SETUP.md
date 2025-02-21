## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <project-directory>
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root and add the following variables:
   ```

   # PostgreSQL credentials
   PGHOST=your_db_host
   PGDATABASE=your_db_name
   PGUSER=your_db_username
   PGPASSWORD=your_db_password

   # Clerk credentials


   # SQL credentials
   DB_USERNAME=your_db_username
   DB_PASSWORD=your_db_password
   DB_HOST=your_db_host
   DB_NAME=acm_education_db
   ```


5. Run the application:
   ```
   python run.py
   ```

   
The application will be available at `http://localhost:5000`.
