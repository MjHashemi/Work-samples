from collections import OrderedDict
num = int(input())
words = OrderedDict()
list_word = []
for n in range(num):
  tr_word = input().split(' ')
  list_word.append(tr_word)
for b in list_word: 
   for i in b[1:]:
      words[i] = b[0]  
sentence=input().split(' ')
jomle=[]
for word in sentence:
  if word in words.keys():
    jomle.append(words[word])
  else:
    jomle.append(word) 
for d in jomle:   
  print(d , end =' ')