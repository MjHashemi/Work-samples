from datetime import datetime

birthday = str(input())
format = "%Y/%m/%d"
try:
  chek_format = bool(datetime.strptime(birthday, format))
except ValueError:
  chek_format = False
if chek_format == False:
  print('WRONG')
else:
  birthday_date = datetime.strptime(birthday, "%Y/%m/%d")
  now = datetime.today()
  age = now - birthday_date
  age = age.days//365
  if age < 0:
    print('WRONG')
  else:
    print(age)
