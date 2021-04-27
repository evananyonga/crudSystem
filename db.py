import psycopg2

# connect to the database
con = psycopg2.connect(
    host="localhost",
    database="blogdb",
    user="postgres",
    password="@llahu", )

# close the database
con.close()
