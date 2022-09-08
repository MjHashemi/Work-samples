Sentence = input()
Words = Sentence.split()
Words.append("a")
Words[0] = "the"
for e in range(len(Words)):           
    if Words[e][-1] == ".":        
        x = Words.index(Words[e+1])
        Words[x] = Words[x].replace(Words[x],"the") 
for a in range(len(Words)):
    if Words[a][-1] == "." :    
        Words[a] = Words[a][:-1]
    if Words[a][-1] == "," :    
        Words[a] = Words[a][:-1]
con = 0   
for c , d in enumerate(Words,1):    
    if d.istitle():
        con += 1
        print(c,d, sep= ":")
if con == 0:
    print("None")