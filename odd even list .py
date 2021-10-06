            

a=[1,2,[3,8,12],[6,7,8,9,10,11]]
i=0
sum=0
while i<len(a):
    b=a[i]
    if type(b)==list:
        for j in range (len(b)):
            if a[j]%2==0:
                print("even no",a[j])

            else:
                print("odd no",a[j])
    else:
        print("not")
    i+=1