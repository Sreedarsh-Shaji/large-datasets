import psycopg2
from faker import Faker
import time
import random

conn = psycopg2.connect(database = "data-engg-learning", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "postgres",
                        port = 5432)

cur = conn.cursor()
fake = Faker()
authority_levels = [1,2,3,4,5]

print("***CREATING 50 ADMINS***")

for i in range(0,35):
    print(f"Executing the {i}th entry!!!")
    
    phone_number = fake.country_calling_code() + " " + fake.phone_number()
        
    first_name = fake.first_name()
    last_name = fake.last_name()
    
    name = f"{first_name} . {last_name}"
    password = fake.password()
    uid = fake.uuid4()
    level = random.choice(authority_levels)
    
    
    values = f"({i+1} , '{name}' ,'{password}','{uid}',{level})"
    
    query = """INSERT INTO public.admin(
	admin_id, user_name, password, "auth_uniqueId", authority_level)""" + " VALUES " + values
 
    print(f"EXECUTING {i+1} -> {query}")
 
    cur.execute(query = query)
    
    time.sleep(30)
    
    
conn.commit()
cur.close()
conn.close()
##### FINISHED IN LOCAL