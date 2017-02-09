def readIt(name):
    f = open(name, "r")
    contents = f.read().strip()
    f.close()
    return contents

def listify(string):
    lis = string.split("\n")
    return lis

def getListOfIDs(lis):
    ret = []
    for line in lis:
        ret.append(line.split(",")[0])
    return ret

def makeD(lis):
    d = {}
    for subLis in lis:
        info = subLis.split(",")
        d[info[0]] = info[1].strip()
    return d



event = makeD(listify(readIt("event.csv")))
hours = getListOfIDs(listify(readIt("hours.csv")))

print hours

for ID in hours:
    ID = ID.strip()
    if ID in event.keys():
        print event[ID]
    print "<br>"

