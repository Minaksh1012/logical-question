a="w3resource"
dict={}
for x in a:
    keys=dict.keys()
    if x in keys:
        dict[x]+=1
    else:
        dict[x]=1    
print(dict)
    



