num=int(input('Enter a number:'))

n=num
su=0
while n>0:
  d=n%10
  su+=d*d*d
  n=n//10

if su==num:
 print("Armstrong Number")
else:
 print("Not a Armstrong Number")