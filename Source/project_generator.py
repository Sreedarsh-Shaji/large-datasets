
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
print("Generating project names")

fake = Faker()

for i in range(1,1864):
    if(i%100 == 0):
        conn.commit()
        time.sleep(2)
        
    start_date = fake.date_time_between(start_date=datetime.datetime(2000, 1, 1, 00, 00, 00),end_date="now")
    end_date = fake.date_time_between(start_date=datetime.datetime(start_date.year+1, start_date.month+1 if start_date.month<12 else 1 , 1, 00, 00, 00),end_date="now")
        
    query = f"""INSERT INTO public.project(id, name, customer, start_date, end_date) VALUES ({i}, '{fake.bs()}', {random.randint(1,85)} , '{start_date}', '{end_date}')"""
    cur.execute(query = query)

print(f"Completed 100%")
print("COMPLETED EXECUTING THE FAKER!!!") 
cur.close()
conn.close()