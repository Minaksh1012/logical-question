a=[1,4,7,6,9,8,9]
i=0
b=[]
while i<len(a):
    if a not in b:
        b.append(a)
    i+=1
print(b)
# i+=1    