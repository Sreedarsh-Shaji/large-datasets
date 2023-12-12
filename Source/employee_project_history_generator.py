
import psycopg2
from faker import Faker
import time
import random
import datetime

#Reading all session id from the database

conn = psycopg2.connect(database = "data-engg-learning", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "postgres",
                        port = 5432)

cur = conn.cursor()
print("Reading all of the employees ids to a list")
query = 'SELECT _id, current_project FROM public.employee'
cur.execute(query = query)
result = cur.fetchall()
employee_proj_map = {i[0]:i[1] for i in result}

fake = Faker()

count = 0

for i in employee_proj_map:
    count = count + 1
    
    query = f"""INSERT INTO public.employee_project_history(id, project_id, emp_id)	VALUES ({count}, '{employee_proj_map[i]}', '{i}')"""
    cur.execute(query = query)
    
conn.commit()

cur.close()
conn.close()