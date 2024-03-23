import csv 


f1 = open("newfile.csv" , "w")
w = csv.writer(f1)


with open("Virtual Fitting Dataset - Sheet1.csv") as f:
    r = csv.reader(f)

    for line in r:
        l=[]
        i=0
        x=0
        try:

            for m in line:
                if i==2:
                    x = m
                    a = int(m) - 5
                    l.append(a)
                elif i==3:
                    l.append(x)
                else:
                    l.append(m)
                i+=1
        except:
            pass
        w.writerow(l)
        
f1.close()