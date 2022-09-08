import mysql.connector
import re

cnx = mysql.connector.connect(user='root', password='1234',
                              host='127.0.0.1',
                              database='usern')
username = input()
password = input()
pattern = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
cursor = cnx.cursor()
while True:  
  if re.match(pattern, username):  
    cursor.execute("insert into user(username,password) values('{}','{}')".format(username,password))  
    break                    
  else:
    print('expression@string.string') 
    username = input() 
    
cnx.commit()  
cnx.close()