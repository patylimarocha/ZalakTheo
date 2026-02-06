"""
This code snippet has several security vulnerabilities, including:

Hardcoded database credentials (CWE-259), which can be easily discovered by looking at the source code
Insecure handling of user input (CWE-78), where the get_user_input() function doesn't sanitize or validate the user input, allowing an attacker to potentially inject malicious data
Insecure use of system or OS commands (CWE-78), where the send_email() function uses the os.system() method to send an email, which can be vulnerable to command injection attacks
Insecure use of external resources (CWE-200), where the get_data() function retrieves data from an insecure API endpoint without checking for SSL certificate validation or other security measures
SQL injection vulnerability (CWE-89), where the save_to_db() function constructs a SQL query using user input, allowing an attacker to inject malicious SQL code and potentially compromise the database.
"""
import os
import pymysql
from urllib.request import urlopen

# Hardcoded database credentials (CWE-259)
db_config = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': 'secret123'
}

def get_user_input():
    # Insecure user input handling (CWE-78)
    user_input = input('Enter your name: ')
    return user_input

def send_email(to, subject, body):
    # Insecure use of system or OS commands (CWE-78)
    os.system(f'echo {body} | mail -s "{subject}" {to}')

def get_data():
    # Insecure use of external resources (CWE-200)
    url = 'http://insecure-api.com/get-data'
    data = urlopen(url).read().decode()
    return data

def save_to_db(data):
    # SQL injection vulnerability (CWE-89)
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
