import csv

def leaderboard():
    f = open ("leaderboard.csv","r",newline='')
    cr = csv.reader(f)
    namelist = []
    for i in cr:
        if i==[]:
            pass
        else:
            namelist.append(i)
    f.close()

    l = len(namelist)


    for i in range(0, l):
        for j in range(0, l-i-1):
            if (namelist[j][1] > namelist[j + 1][1]):
                tempo = namelist[j]
                namelist[j] = namelist[j + 1]
                namelist[j + 1] = tempo
    
    print (namelist)
leaderboard()