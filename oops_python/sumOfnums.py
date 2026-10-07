n = int(input("Enter the elements (N):"))
arr = []
print("Enter the integers:")
for i in range(n):
    num = int(input())
    arr.append(num)
print("The sum of all elements is:", sum(arr))
