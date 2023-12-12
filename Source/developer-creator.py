import psycopg2
from faker import Faker

conn = psycopg2.connect(database = "data-engg-learning", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "postgres",
                        port = 5432)

cur = conn.cursor()

cur.execute("SELECT * FROM admin")
print("Connection established successfully")

conn.commit()

cur.close()
conn.close()