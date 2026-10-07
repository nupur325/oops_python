num=int(input("Enter a number:"))
flag=0
for i in range(2,(num//2)+1):
    if (num%i==0):
        flag=1
        break
if(flag==0):
    print("Prime number")
else:
    print("Not prime")


#Logic
# flag=0
# for(i=2;i<num;i++):
#     if (num%i==0):
#     flag=1
#     break;
# if(flag==0):
#     print("Prime number")
# else:
#     print("Not prime")