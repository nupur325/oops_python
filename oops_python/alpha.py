s = input("ENter a string: ")
vowel=0
consonant=0
digits=0
char=0
vowels="aAeEiIoOuU"
for c in s:
    if c.isalpha():
        if c in vowels:
            vowel+=1
        else:
            consonant+=1
    elif c.isdigit():
        digits+=1
    else:
        char+=1
print("Vowels:", vowel)
print("Consonants:", consonant)
print("Digits:", digits)
print("Special Characters:", char)
