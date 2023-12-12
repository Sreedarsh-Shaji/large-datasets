
import psycopg2
from faker import Faker
import time
import random
import datetime
import string

#Reading all session id from the database

conn = psycopg2.connect(database = "data-engg-learning", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "postgres",
                        port = 5432)

cur = conn.cursor()
print("Reading all of the session ids to a list")

fake = Faker()

project_history_queries = []
employee_manager_queries = []

for i in range(1,2368):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = last_name + "." + first_name + "@cleardesk.com"
    added_by = random.randint(1,500)
    approved_by = random.randint(1,35)
    date_of_addition = fake.date_time_between(start_date=datetime.datetime(2000, 1, 1, 00, 00, 00),end_date="now")
    date_of_approval = fake.date_time_between(start_date=date_of_addition,end_date=datetime.datetime(date_of_addition.year, 
                                                                                                     date_of_addition.month, 
                                                                                                     date_of_addition.day + 3 if date_of_addition.day <= 25 else date_of_addition.day, 
                                                                                                     date_of_addition.hour + 1 if date_of_addition.hour <= 22 else 1, 00, 00))
    current_project = random.randint(1,1799)
    allocation_date = fake.date_time_between(start_date=date_of_approval,end_date=datetime.datetime(date_of_approval.year, 
                                                                                                     date_of_approval.month, 
                                                                                                     date_of_approval.day + 3 if date_of_approval.day <= 25 else date_of_approval.day, 
                                                                                                     date_of_approval.hour + 1 if date_of_approval.hour <= 22 else 1, 00, 00))
    _ID = 'TE-' + ''.join(random.choice(string.ascii_uppercase)) + "-" + ''.join(random.choices(string.digits,k=8))
    PAN = ''.join(random.choices(string.ascii_uppercase, k=6) + random.choices(string.digits, k=3) + random.choices(string.ascii_uppercase, k=1)) #Intentionally generating 6 characters insted of 5 to avoid generating valid PAN
    AADHAR = ''.join(random.choices(string.digits,k=12))
    reporting_manager = random.randint(1,i)
    
    if(i%100 == 0):
        print(f"Completed {(i/2365)*100}%")
        conn.commit()
        time.sleep(2)
        
    query = f"""INSERT INTO public.employee(
	_id, first_name, last_name, email_id, added_by, approved_by, date_of_addition, date_of_approval, role, aadhar_card_number, pan, current_project, allocated_date)
	VALUES ('{_ID}', '{first_name}' , '{last_name}' , '{email}' , { added_by } , {approved_by} , '{date_of_addition}' , '{date_of_approval}' , {random.randint(1,5)} , '{AADHAR}', '{PAN}', '{current_project}', '{allocation_date}')"""
 
    
 
    # query1 = f"INSERT INTO public.employee_project_history(id, project_id, emp_id) VALUES ({i}, '{current_project}', '{_ID}')"
    # project_history_queries.append(query1)
    
    # query2 = f"""INSERT INTO public."employee-manager"(emp_id, manager_id) VALUES ('{_ID}', {reporting_manager})"""
    # employee_manager_queries.append(query2)
 
    cur.execute(query = query)
    # # cur.execute(query = query1)
    # cur.execute(query = query2)
    
print("Added the employee details to db!")
conn.commit()
    
# for i in project_history_queries:
#     cur.execute(i)
# print("Added the project history details to db!")
# conn.commit()
    
# for i in employee_manager_queries:
#     cur.execute(i)
# print("Added the employee manager details to db!")
# conn.commit()    
    

print(f"Completed 100%")
print("COMPLETED EXECUTING THE EMPLOYEE DETAILS FAKE INSERTION!!!") 
cur.close()
conn.close()