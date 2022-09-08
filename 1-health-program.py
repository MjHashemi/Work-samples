class School: 
  def __init__(self): 
    self.n =int(input()) 
    list_ages = [float(x) for x in input().split()] 
    list_hight = [float(x) for x in input().split()] 
    list_weight = [float(x) for x in input().split()]     
    self.list_ages, self.list_hight, self.list_weight = zip(
      *zip( list_ages,list_hight,list_weight ))

  def get_av(self):
    self.avg_age = sum(self.list_ages) / len(self.list_ages)
    print(self.avg_age)
    self.avg_height = sum(self.list_hight) / len(self.list_hight)
    print(self.avg_height)
    self.avg_weight = sum(self.list_weight) / len(self.list_weight)
    print(self.avg_weight)  
    return  self.avg_age, self.avg_height, self.avg_weight


  def compare(self,other):
    self.get_av()
    other.get_av()    
    if self.avg_height > other.avg_height:
      print('A')
    elif self.avg_height < other.avg_height:
      print('B')
    elif self.avg_height == other.avg_height:
      if self.avg_weight > other.avg_weight:
        print('B')
      elif self.avg_weight < other.avg_weight:
        print('A')
      elif self.avg_weight == other.avg_weight:
        print('Same')

A = School() 
B = School()

A.compare(B)