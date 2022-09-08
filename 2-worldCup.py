teams ={
"iran" : {'name': 'Iran', 'wins':0, 'loses':0, 'draws':0, 'goal difference':0, 'points':0},
"spain" : {'name': 'Spain', 'wins':0, 'loses':0, 'draws':0, 'goal difference':0, 'points':0},
"morocco": {'name': 'Morocco', 'wins':0, 'loses':0, 'draws':0, 'goal difference':0, 'points':0},
"portugal" : {'name': 'Portugal', 'wins':0, 'loses':0, 'draws':0, 'goal difference':0, 'points':0}}
gollist = []
for i in range(6):    
    x = input().split("-")
    gollist.append(x)

goollist =[]
for sublist in gollist:
	for a in sublist:
		a = int(a)
		goollist.append(a)

if goollist[0] == goollist[1]:
    teams ["iran"]["draws"] += 1
    teams ["iran"]["points"] += 1
    teams ["spain"]["draws"] += 1
    teams ["spain"]["points"] += 1
elif goollist [0] > goollist[1]:
    teams ["iran"]["wins"] += 1
    teams ["iran"]["points"] += 3
    teams ["spain"]["loses"] += 1
elif goollist [0] < goollist[1]:
    teams ["iran"]["loses"] += 1
    teams ["spain"]["wins"] += 1
    teams ["spain"]["points"] += 3
if goollist[2] == goollist[3]:
    teams ["iran"]["draws"] += 1
    teams ["iran"]["points"] += 1
    teams ["portugal"]["draws"] += 1
    teams ["portugal"]["points"] += 1
elif goollist[2] > goollist[3]:
    teams ["iran"]["wins"] += 1
    teams ["iran"]["points"] += 3
    teams ["portugal"]["loses"] += 1
elif goollist[2] < goollist[3]:
    teams ["iran"]["loses"] += 1
    teams ["portugal"]["wins"] += 1
    teams ["portugal"]["points"] += 3
if goollist[4] == goollist[5]:
    teams ["iran"]["draws"] += 1
    teams ["iran"]["points"] += 1
    teams ["morocco"]["draws"] += 1
    teams ["morocco"]["points"] += 1
elif goollist[4] > goollist[5]:
    teams ["iran"]["wins"] += 1
    teams ["iran"]["points"] += 3
    teams ["morocco"]["loses"] += 1
elif goollist[4] < goollist[5]:
    teams ["iran"]["loses"] += 1
    teams ["morocco"]["wins"] += 1
    teams ["morocco"]["points"] += 3
if goollist[6] == goollist[7]:
    teams ["spain"]["draws"] += 1
    teams ["spain"]["points"] += 1
    teams ["portugal"]["draws"] += 1
    teams ["portugal"]["points"] += 1
elif goollist[6] > goollist[7]:
    teams ["spain"]["wins"] += 1
    teams ["spain"]["points"] += 3
    teams ["portugal"]["loses"] += 1
elif goollist[6] < goollist[7]:
    teams ["spain"]["loses"] += 1
    teams ["portugal"]["wins"] += 1
    teams ["portugal"]["points"] += 3
if goollist[8] == goollist[9]:
    teams ["spain"]["draws"] += 1
    teams ["spain"]["points"] += 1
    teams ["morocco"]["draws"] += 1
    teams ["morocco"]["points"] += 1
elif goollist[8] > goollist[9]:
    teams ["spain"]["wins"] += 1
    teams ["spain"]["points"] += 3
    teams ["morocco"]["loses"] += 1
elif goollist[8] < goollist[9]:
    teams ["spain"]["loses"] += 1
    teams ["morocco"]["wins"] += 1
    teams ["morocco"]["points"] += 3
if goollist[10] == goollist[11]:
    teams ["portugal"]["draws"] += 1
    teams ["portugal"]["points"] += 1
    teams ["morocco"]["draws"] += 1
    teams ["morocco"]["points"] += 1
elif goollist[10] > goollist[11]:
    teams ["portugal"]["wins"] += 1
    teams ["portugal"]["points"] += 3
    teams ["morocco"]["loses"] += 1
elif goollist[10] < goollist[11]:
    teams ["portugal"]["loses"] += 1
    teams ["morocco"]["wins"] += 1
    teams ["morocco"]["points"] += 3
teams ["iran"]["goal difference"] = (goollist[0]+goollist[2]+goollist[4]) - (goollist[1]+goollist[3]+goollist[5])
teams ["spain"]["goal difference"] = (goollist[1]+goollist[6]+goollist[8]) - (goollist[0]+goollist[7]+goollist[9])
teams ["portugal"]["goal difference"] = (goollist[3]+goollist[7]+goollist[10]) - (goollist[2]+goollist[6]+goollist[11])
teams ["morocco"]["goal difference"] = (goollist[5]+goollist[9]+goollist[11]) - (goollist[4]+goollist[8]+goollist[10])
sorted_teams = sorted(teams.items(), key=lambda x: (-x[1].get('points'), -x[1].get('wins'), x[1].get('name')))

Result = []
for z in sorted_teams: 
    Result.append(z[1])

for y in Result:
    print(y["name"], end= "  ")
    print('{}{}'.format("wins:",y["wins"]), end=" , ")
    print('{}{}'.format("loses:",y["loses"]), end=" , ")
    print('{}{}'.format("draws:",y["draws"]), end=" , ")
    print('{}{}'.format("goal difference:",y["goal difference"]), end=" , ")
    print('{}{}'.format("points:",y["points"]))