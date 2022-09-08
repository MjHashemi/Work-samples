dict_Genre = {"Horror": 0 , "Romance": 0, "Comedy": 0, "History": 0, "Adventure": 0, "Action": 0}
person_number = int(input())
NG = []
for a in range(person_number):
    name = input().split(" ")
    NG.append(name)
Name_Genre = []
for b in NG:
    for c in b:
        Name_Genre.append(c)
for d in Name_Genre:   
    c = Name_Genre.count("Horror")
    dict_Genre.update({"Horror": c})
    d = Name_Genre.count("Romance")
    dict_Genre.update({"Romance":d})
    e = Name_Genre.count("Comedy")
    dict_Genre.update({"Comedy":e})
    f = Name_Genre.count("History")
    dict_Genre.update({"History":f})
    g = Name_Genre.count("Adventure")
    dict_Genre.update({"Adventure":g})
    h = Name_Genre.count("Action")
    dict_Genre.update({"Action":h})
sorted_dict_Genre = sorted(dict_Genre.items(), key=lambda x: (-x[1], x[0]))
for index, tuple in enumerate(sorted_dict_Genre):
	element_one = tuple[0]
	element_two = tuple[1]
	print(element_one," : ", element_two)