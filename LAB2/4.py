x=input("Enter a sentence: ")
l=[]
for i in range(0,len(x)):
    y=10*ord(x[i])+2
    l.append(y)

print(l)