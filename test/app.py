import sqlite3
import csv 


# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('body_shapes.db')
cursor = conn.cursor()

# Create a table to store the data
cursor.execute('''CREATE TABLE IF NOT EXISTS body_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    bust REAL,
                    waist REAL,
                    high_hip REAL,
                    hip REAL,
                    predicted_body_shape TEXT
                )''')

# Define the JavaScript functions in Python
def calculate(bust, waist, high_hip, hip):
    inch_to_cm = lambda inch: inch * 2.54

    bust_hips = (bust - hip)
    hips_bust = (hip - bust)
    bust_waist = (bust - waist)
    hips_waist = (hip - waist)
    high_hip_waist = (high_hip - waist)

    body_type = "Hourglass"
    if (hips_bust >= inch_to_cm(3.6) and hips_bust < inch_to_cm(10) and hips_waist >= inch_to_cm(9) and high_hip_waist < inch_to_cm(1.193)):
        body_type = 'Bottom Hourglass'
    if (bust_hips > inch_to_cm(1) and bust_hips < inch_to_cm(10) and bust_waist >= inch_to_cm(9)):
        body_type = 'Top Hourglass'
    if (hips_bust > inch_to_cm(2) and hips_waist >= inch_to_cm(7) and high_hip_waist >= inch_to_cm(1.193)):
        body_type = 'Spoon'
    if (hips_bust >= inch_to_cm(3.6) and hips_waist < inch_to_cm(9)):
        body_type = 'Triangle'
    if (bust_hips >= inch_to_cm(3.6) and bust_waist < inch_to_cm(9)):
        body_type = 'Inverted triangle'
    if (hips_bust < inch_to_cm(3.6) and bust_hips < inch_to_cm(3.6) and bust_waist < inch_to_cm(9) and hips_waist < inch_to_cm(10)):
        body_type = 'Rectangle'
    
    return body_type

# Insert data into the database
def insert_data(l):
    bust , waist , high_hip , hip = l[0] ,l[1] , l[2] , l[3]
    predicted_body_shape = calculate(bust, waist, high_hip, hip)
    cursor.execute("INSERT INTO body_data (bust, waist, high_hip, hip, predicted_body_shape) VALUES (?, ?, ?, ?, ?)",
                   (bust, waist, high_hip, hip, predicted_body_shape))
    conn.commit()

# Example usage
with open("newfile.csv" , "r") as f:
    r = csv.reader(f)
    for line in r:
        try:
            insert_data(line)
        except:
            pass


        

# Fetch data from the database
cursor.execute("SELECT * FROM body_data")
data = cursor.fetchall()
for row in data:
    print(row)

# Close the database connection
conn.close()
