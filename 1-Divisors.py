Numbers = []
for a in range(10):
    num = int(input())
    Numbers.append(num)
divis = []
dictperim = {}
for a in Numbers:
    i = 1    
    div = []
    c = 0
    while i <= a :                
        if a % i == 0:
            div.append(i)
            c += 1
        i += 1
    divis.append(div)
    perim = [] 
    for b in div:        
        count = 0       
        for f in range(1 , b + 1):
            if b % f == 0:
                count += 1
        if count == 2:
            perim.append(b)
        else:
            continue 
    dictperim.update({a : len(perim)})
    javab = max(dictperim.items(), key = lambda x:(x[1],x[0]))
print(*javab,sep=' ')