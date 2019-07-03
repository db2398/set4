t=int(input())
e1,e2=0,1
print(e2,end=" ")
for i in range(1,t):
 e3=e1+e2
 print(e3,end=" ")
 e1,e2=e2,e3
