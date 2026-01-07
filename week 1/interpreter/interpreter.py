expression = input("Expression: ")

x, op, z = expression.split()

x = float(x)
z = float(z)

if op == "+":
    result = x + z
elif op == "-":
    result = x - z
elif op == "*":
    result = x * z
elif op == "/":
    result = x / z
else :
    print("Something went wrong")

print(f"{result:.1f}")
