import sqlite3

# Connect to the database
conn = sqlite3.connect('body_shapes.db')

# Create a cursor object
cursor = conn.cursor()

# Execute SQL queries
cursor.execute('SELECT * FROM body_data')

# Fetch results
results = cursor.fetchall()

# Close the connection
conn.close()
