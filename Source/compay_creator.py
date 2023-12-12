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
authority_levels = [1,2,3,4,5]

print("***CREATING 50 ADMINS***")

for i in range(0,85):
    print(f"Executing the {i}th entry!!!")
    
    company_name = fake.company()
    
    values = f"({i+1} , '{company_name}')"
    
    query = """INSERT INTO public.customer(id, name)""" + " VALUES " + values
 
    print(f"EXECUTING {i+1} -> {query}")
 
    cur.execute(query = query)
    
    time.sleep(30)
    
    
conn.commit()
cur.close()
conn.close()