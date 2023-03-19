desh = ["bangladesh", "india", "pakistan", "sri lanka", "nigeria", "uganda"]
raja = ["tania", "mimi", "arif", "mubin"]
for raja in raja:
    for desh in desh:
        if raja[-1]== desh[0]:
            print(raja, "is the king of", desh)
