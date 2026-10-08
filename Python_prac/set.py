#set declared using {}
#set is unordered and hence doesn't have indexing
marks = {95,92,94,92}
person = 'ram','shyam','geeta' #set doesnt necessarily need paranthesis 
print(person)
print(marks) 
#set stores unique values only and hence duplicates afre not printed

#print(marks[0]) --indexing is not valid in sets

for s in marks: #you can iterate tho
    print(s)
