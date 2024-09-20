#Marco Quintero
#AMA
#SoftDev
#K06 -- Read from file, return job class based on specified percentage in data set
#Time spent: 0.8

import random
fCVS = open("occupations.csv")

stf = fCVS.read().strip()
dicts = {}


def createDict(text):
    #print(text)
    l = text.split("\n")
    #print(l)
    pair = []
    
    for i in range(1,len(l) - 1):
        if l[i][0] == '"':
            pair = l[i].split('",')
            pair[0] = pair[0][1:]
            print(pair)
            dicts[pair[0]] = float(pair[1])
        else:
            pair = l[i].split(',')
            pair[0] = pair[0]
            print(pair)
            dicts[pair[0]] = float(pair[1])
            
    print(dicts)
    print(len(dicts))
    
def randJob(lst):
    print(random.choices(list(lst.keys()), weights = list(lst.values()), k = 50))
createDict(stf)
randJob(dicts)

