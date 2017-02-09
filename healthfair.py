offset = 6
teachers = {
    "brown" : 6,
    "cimaglia" : 7,
    "choy" : 8,
    "fang" : 9,
    "garber" : 10,
    "genkina" : 11,
    "greenwald" : 12,
    "hanna" : 13,
    "hill" : 14,
    "horenstein" : 15,
    "kats" : 16,
    "madden" : 17,
    "maggio" : 18,
    "markova" : 19,
    "miller" : 20,
    "montserrat" : 21,
    "quenzer" : 22,
    "reep" : 23,
    "siegel" : 24,
    "sterr" : 25,
    "thomas" : 26,
    "ting" : 27,
    "vargo" : 28
}

students = []

for i in range(23):
    students.append([])
    
print students

def readIt(name):
    f = open(name, "r")
    contents = f.read().strip()
    f.close()
    return contents

def listify(string):
    lis = string.split("\n")
    length = len(lis)
    i = 0
    return lis

def makeD(lis):
    d = {}
    for subLis in lis:
        info = subLis.split(",")
        d[info[1].strip()] = info[0].strip()
    return d

def makeDEC(lis):
    d = {}
    for subLis in lis:
        info = subLis.split(",")
        d[info[4].strip()] = [info[1:4], info[6:29] ]
    return d

def makelists(final):
    for teacher in teachers.keys():
        fname = teacher + ".csv"
        f = open(fname, "w")

        i = teachers[teacher] - offset
    #    print teacher, i
    #    print i
        
        for student in final.keys():
     #       print "i", i
            pd = final[student][2][i]
            if len(pd) == 1 or len(pd) == 2:
                info = ",".join(final[student][0]) + "," + student + "," + pd + "," + ",".join(final[student][1]) + "\n"
                f.write(info)
       #         print teacher
       #         print info
    
        f.close()




signin = makeD(listify(readIt("signin.csv")))
signout = makeD(listify(readIt("signout.csv")))

ec = makeDEC(listify(readIt("ec.csv")))
#key: osis, value: [[email, fname, lname], [brown, cimaglia, ..., vargo]]

#print ec

final = {}
amt  = 0
for key in ec.keys():
    if key in signin and key in signout:
        final[key] = [ ec[key][0], [signin[key], signout[key]], ec[key][1] ]
        amt += 1

#print final
makelists(final)
        
#print final
#print amt
