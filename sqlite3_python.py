import sqlite3

conn = sqlite3.connect('hotels.db')
c = conn.cursor()
c.execute("SELECT * FROM hotels WHERE area='south' AND price='high'")
c.fetchall()
# => [('Grand Hotel', 'high', 'south', 5)]

# SQL Injection potential
query = "SELECT name FROM restaurants WHERE area={}".format(area)
c.execute(query)

# Better
t = (area, price)
c.execute('SELECT name FROM restaurants WHERE area=? and price=?', t)


import sqlite3
conn = sqlite3.connect('hotels.db')
c = conn.cursor()
area, price = "south", "hi"
t = (area, price)
c.execute('SELECT * FROM hotels WHERE area=? AND price=?', t)
print(c.fetchall())



