num=int(input("Enter a number:"))
rev=0
n=num
while(n>0):
    rev=rev*10+(n%10)
    n=n//10
print(rev)
if(num==rev):
    print("Number is Palindrom")
else:
    print("Not a palindrome")
