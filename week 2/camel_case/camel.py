camelCase_vrble = input("camelCase: ")

snake_variable = ""

for letter in camelCase_vrble:
    if letter.isupper():
        snake_variable += "_" + letter.lower()
    else:
        snake_variable += letter

print(snake_variable)
