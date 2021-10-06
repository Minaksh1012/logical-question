
for i in range(1,10):
    n=input("u can enter small and captial alphabet")
    if (n>="a" or n<="z") and (n>="A" or n<="Z"):
        print(n)
        char=input("enter the char")
        if char=="#" or char=="@" or char=="&":
            print(char)
            num=int(input("enter the num"))
            if num>=0 or num<=9:
                print(n+char+str(num))
                break
            else:
                print("no")
        else:
            print("its not char")
    else:
        print("this is not alphabet")



# n=input("enter the alphbet")
# i=1
# while i<len(n):
#     if n>="a" or n<="z":
#         print(n)
#         char=input("enter the char")
#         if char=="#" or char=="@" or char=="&":
#             print(char)
#             num=int(input("enter the num"))
#             if num>=0:
#                 print(n+char+str(num))
#                 break
#             else:
#                 print("no")
#         else:
#             print("its not char")
#     else:
#         print("this is not alphabet") 
#     i+=1