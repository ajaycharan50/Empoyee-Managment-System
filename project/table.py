import mysql.connector


# Replace 'your_host', 'your_username', 'your_password', and 'your_database' with your actual MySQL connection details.
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Ajay@123',
    database='ajay'
)


cursor = db_connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT,
    email VARCHAR(255)
)
"""

cursor.execute(create_table_query)
db_connection.commit()

cursor.close()
db_connection.close()
