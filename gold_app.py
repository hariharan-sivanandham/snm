import sqlite3
conn = sqlite3.connect(r"C:\Users\Admin\Desktop\gold.db")
cursor = conn.cursor()
print("Connected successfully!")
cursor.execute("SELECT * FROM gold_slabs")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()
