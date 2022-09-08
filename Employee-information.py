import mysql.connector

cnx = mysql.connector.connect(user='root', host='127.0.0.1',database='employee')

cursor = cnx.cursor()
query = 'SELECT * FROM employee ORDER BY Height DESC, Weight ASC;'
cursor.execute(query)
for (Name,Height,Weight) in cursor:
  print("%s %s %s" % (Name, Height, Weight))  
cnx.close()

