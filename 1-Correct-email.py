import re 

email = input()
pattern = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
if re.match(pattern, email):  
  print('OK')                   
else:    
  print('WRONG')  