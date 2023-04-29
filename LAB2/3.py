t1=("Orange","Apple","Grapes","Apple","Orange")
t2=[]

for i in range(0,len(t1)):
    x= t1.count(t1[i])
    if x>1:
        t2.append(t1[i])
t3=set(t2)
print(t3)
        


