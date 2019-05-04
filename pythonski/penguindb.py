import sqlite3
conn=sqlite3.connect('products.db')
c=conn.cursor()
c.execute("INSERT INTO products values('Caraval',267.50,'Scarlett Dragna has never left the tiny island where she and her sister, Tella, live with their powerful, and cruel, father.','https://images.gr-assets.com/books/1465563623l/27883214.jpg')")
conn.commit()
conn.close()
#for row in c.execute("SELECT * FROM products"):
'''  
for row in c.execute("SELECT * FROM products"):
    temp = dict()
    name = row[0]
    price = row[1]
    desc = row[2]
    temp['name'] = name
    temp['price'] = price
    temp['description'] = desc
    products.append(temp)
print (products)
'''