import psycopg2
from faker import Faker
import time

conn = psycopg2.connect(database = "data-engg-learning", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "postgres",
                        port = 5432)

cur = conn.cursor()
fake = Faker()

for i in range(0,500):
    print(f"Executing the {i}th entry!!!")
    
    phone_number = fake.country_calling_code() + " " + fake.phone_number()
        
    first_name = fake.first_name()
    last_name = fake.last_name()
    
    name = f"{first_name} . {last_name}"
    email = f"{first_name}@cleardesk.com"
    
    values = f"({i+1} , 'MBA - HR/LABOR LAWS' ,'{phone_number}','{email}','{name}')"
    
    query = """INSERT INTO public.managament_employee_profile(
	profile_id, qualification, official_phone, official_public_email,name)""" + " VALUES " + values
 
    cur.execute(query = query)
 
    print(f"EXECUTING {i+1} -> {query}")
    
    time.sleep(10)
    
    
conn.commit()
cur.close()
conn.close()