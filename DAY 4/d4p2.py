l=[]
n=int(input("Size of tuple : "))
for i in range(n):
a=input("Enter the element : ")
l.append(a)
l.sort()
t=tuple(l)
print(t)