############
#ASSIGNMENT#
############
CREATE TABLE employees (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    position ENUM('PM','Frontend','Backend'),
    salary DECIMAL(10,2)
);

INSERT INTO employees (name, position, salary) VALUES 
	('혜린', 'PM', 90000),
    ('은우', 'Frontend', 80000),
    ('가을', 'Backend', 92000),
    ('지수', 'Frontend', 78000),
    ('민혁', 'Frontend', 96000),
    ('하온', 'Backend', 130000);

#name salary
CREATE TABLE  epl_ns2 AS 
SELECT name, salary 
FROM employees

#FRontend Emplyess
CREATE TABLE Frontend_eplyX AS
SELECT name, salary 
FROM employees
WHERE position = 'Frontend'

#PM salary*10
SET SQL_SAFE_UPDATES = 0; #Unlock SAFE MODE
UPDATE employees SET salary = salary*1.1  WHERE position = 'PM';
SELECT * FROM employees

#Backend salary*1.1
UPDATE employees SET salary = salary*1.1  WHERE position = 'Backend';
SELECT * FROM employees;

#delete minhyuk
DELETE FROM employees WHERE name = '민혁';

#Grouping, avg
CREATE TABLE AVG_position AS
SELECT position, AVG(salary)
FROM employeesAVG_position
GROUP BY position

#delete table
DROP TABLE employees


#########
#LECTURE#
#########
import mysql.connector
from faker import Faker
import random #Python Basic Module

# (1) MYSQL Basic Connection
db_connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'As583346!@',
    database = 'testDB'
)

# (2) MYSQL Moudle 연결
cursor = db_connection.cursor()
faker = Faker()

# User Data Gen
for _ in range(30):
    name = faker.user_name()
    email = faker.email()
    age =  random.randrange(30,90)

    #SQL 문 이거 실행해줘
    sql = "INSERT INTO users(name, email, age) VALUES(%s, %s, %s)"
    values = (name, email, age,)

    cursor.execute(sql, values)

####  USER ID _ LOADING
# cursor.execute("SELECT id FROM users")
# valid_user_id = [row[0] for row in cursor.fetchall()]

db_connection.commit()
cursor.close()
db_connection.close()
