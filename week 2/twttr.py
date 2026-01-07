inpt= input("Input: ")
vowels=["a", "e", "i" ,"o", "u", "A", "E", "I", "O", "U"]
result = inpt

for vowel in vowels:
    if vowel in vowels:
        result= result.replace(vowel, "")

print(result)