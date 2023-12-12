import psycopg2
from faker import Faker
import time
import random
import datetime

conn = psycopg2.connect(database = "data-engg-learning", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "postgres",
                        port = 5432)

cur = conn.cursor()
fake = Faker()

print("***CREATING 86448 ADMIN_login history***")

for i in range(0,86448):
    print(f"Executing the {i}th entry!!!")
    
    admin_id = random.randrange(1,36) 
    session_key = fake.uuid4()
    session_stat_date =  fake.date_time_between(start_date=datetime.datetime(2000, 1, 1, 00, 00, 00),end_date="now")
    
    print(f"Start date {session_stat_date}")
    
    end_date = datetime.datetime( session_stat_date.year,
                                 session_stat_date.month,
                                 session_stat_date.day if (session_stat_date.hour <= 20 or session_stat_date.day >= 28)  else session_stat_date.day+1,
                                 session_stat_date.hour + random.randint( 0,6 ) if session_stat_date.hour< 8 else session_stat_date.hour,
                                 session_stat_date.minute + random.randint( 0,6 ) if session_stat_date.minute < 45 else session_stat_date.minute,00
                                 )
    
    session_end_date = fake.date_time_between(start_date=session_stat_date,end_date=end_date)
    
    values = f"({i+1} , '{admin_id}' ,'{session_stat_date}','{session_end_date}','{session_key}')"
    
    query = """INSERT INTO public.admin_login_history(
	session_id, admin_id, login_time, logout_time, session_key)""" + " VALUES " + values
 
    print(f"EXECUTING {i+1} -> {query}")
 
    cur.execute(query = query)
    
    # time.sleep(1)
    
    
conn.commit()
cur.close()
conn.close()