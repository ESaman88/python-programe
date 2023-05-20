d={}
print("how many elements",end=' ')
n=int(input())
for i in range(n):
    print("entering key",end=' ')
    k=input()
    print("enerting values",end=' ')
    v=int(input())
    d.update({k:v})
    print("dictionary is",d)
