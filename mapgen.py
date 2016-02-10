import random
mapfile=open("loccheck2.txt","w")

lr=[]
for z in range(500):
    r=chr(random.randrange(97,102))
    lr.append(r)

for i in range(150):
    line=str(random.randint(-50,50))+' '+str(random.randint(-50,50))+' '+lr[i]
    mapfile.write(line+'\n')
mapfile.close()

unsorted=open("loccheck2.txt","r")
sortedl=open("loccheck.txt","w")
linelist=unsorted.readlines()
linelist.sort()
for lines in linelist:
    sortedl.write(lines)
unsorted.close()
sortedl.close()
