
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
print("Reading all of the session ids to a list")
query = 'SELECT "session_key" FROM public.admin_login_history'
cur.execute(query = query)

#Saving all of the the session ids to a list
session_id_lists = list(i[0] for i in cur.fetchall())

fake = Faker()

for i in range(110000,5000001):
    if(i%1000 == 0):
        print(f"Completed {(i/5000000)*100}%")
        conn.commit()
        time.sleep(2)
        
    query = f"""INSERT INTO public.admin_activity_log(
	activity_log_id, admin_login_session_id, activity_type, time_of_action)
	VALUES ({ i }, {random.randint(1,86448)}, {random.randint(1,6)},' {fake.date_time_between(start_date=datetime.datetime(2000, 1, 1, 00, 00, 00),end_date="now")}')"""
    cur.execute(query = query)

print(f"Completed 100%")
print("COMPLETED EXECUTING THE ADMIN ACTIVITY LOG!!!") 
cur.close()
conn.close()