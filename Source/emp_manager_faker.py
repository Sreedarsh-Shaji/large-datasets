import psycopg2
from faker import Faker
import time
import random

conn = psycopg2.connect(database = "data-engg-learning", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "postgres",
                        port = 5432)
# 2367 
cur = conn.cursor()
fake = Faker()

print("Reading all of the employees ids to a list")
query = 'SELECT _id FROM public.employee'
cur.execute(query = query)
result = cur.fetchall()
employee_id_set = [i[0] for i in result]

for i in employee_id_set:    
    query = f"""INSERT INTO public."employee-manager"(emp_id, manager_id) VALUES ('{i}', '{random.choice(employee_id_set)}')"""
    cur.execute(query = query)
    
conn.commit()
cur.close()
conn.close()