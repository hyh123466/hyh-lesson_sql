import sqlite3
conn = sqlite3.connect('product_info.db')

cursor = conn.cursor()

sqlsel="""
SELECT id, name FROM product_info
WHERE id = '2'
"""
cursor.execute(sqlsel)

cursor.execute('SELECT * FROM product_info')

records = cursor.fetchall()
print (records)

# sqlins="""
# INSERT INTO "main"."product_info"
# ("name", "version", "remark")
# VALUES ('Laptop', 'ASUS', 'I love ASUS');
# """
# cursor.execute(sqlins)
# records = cursor.fetchall()
# conn.commit()

# print (records)

# execute sqlctrl.py
#1: in terminal: python sqlctrl.py
#2: in terminal: python3 sqlctrl.py
#3: in VScode:  click'run python file'