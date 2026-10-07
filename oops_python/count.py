n = int(input("Enter the number of elements: "))
array = []
even=0; odd = 0; 
print(f"Enter {n} integers:")
for i in range(n):
    element = int(input())
    array.append(element)
for num in array:
    if num % 2 == 0:
        even = + 1
    else:
        odd = odd + 1
print("Total even numbers:", even)
print("Total odd numbers:", odd)
