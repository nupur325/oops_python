n=int(input("Enter n numbers:"))
array=[]
print("ENter your numbers:")
for i in range(n):
    num=int(input())
    array.append(num)
print("ENter the element to be searched:")
s=int(input())
if s in array:
    pos = array.index(s)+1
    print("Number is present in the array at position",pos)
else:
    print("Number is not present in the array")
