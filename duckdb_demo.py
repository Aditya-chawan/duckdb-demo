import duckdb


con = duckdb.connect('my_database.db')

con.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER,
        name TEXT,
        age INTEGER
    )
''')

con.execute("INSERT INTO users VALUES (1, 'aditya', 30)")
con.execute("INSERT INTO users VALUES (2, 'Satyam', 25)")
con.execute("INSERT INTO users VALUES (3, 'Gopal', 35)")
con.execute("INSERT INTO users VALUES (4, 'dheerj', 29)")



print("User Data:")
result = con.execute("SELECT * FROM users")
result.df().to_string(index=False)

print("\nUsers older than 28:")
result = con.execute("SELECT name, age FROM users WHERE age > 28")
print(result.df().to_string(index=False))

print("\nAverage age of users:")
result = con.execute("SELECT AVG(age) AS avg_age FROM users")
print(result.df().to_string(index=False))

con.close()