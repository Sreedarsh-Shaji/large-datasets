import psycopg2
from faker import Faker
fake = Faker()


conn = psycopg2.connect(database = "data-engg-learning", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "postgres",
                        port = 5432)

cur = conn.cursor()

for i in range(0,99999):
    
    firstName = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    
    
    
    cur.execute(f"""INSERT INTO public.employee(
	_id, first_name, last_name, email_id, added_by, approved_by, date_of_addition, date_of_approval, role, aadhar_card_number, pan, current_project, allocated_date, reporting_manager)
	VALUES ()""")
    conn.commit()

cur.close()
conn.close()