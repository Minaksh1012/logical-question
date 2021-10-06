# a=[1,2,[3,4,5],[6,7,8,[9,10,11]]]
# a=[1,2,3,[7,8],6]
# list=[]
# i=0
# sum=0
# while i<len(a):
#     n=a[i]
#     if type(n)==list:
#         for j in range (len(n)):
#             # for k in range (len(n)):
#                 sum=sum+n[j]
#             #     sum=sum+n[k]
#     else:
#         sum=sum+n
#     i+=1
# print(sum)                    




a=[1,2,[3,4,5],[6,7,8,9,10,11]]
i=0
sum=0
while i<len(a):
    b=a[i]
    if type(b)==list:
        for j in range (len(b)):
            sum=sum+b[j]
    else:
        sum=sum+a[i]
    i+=1
print(sum)                