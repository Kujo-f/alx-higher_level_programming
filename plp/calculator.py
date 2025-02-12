a = int(input("Enter no. :"))
t = int(input("Enter no. :"))
g = input("Enter operator: ")

result = 0

if g == "+":
    result = a + t
elif g == "-":
    result = a - t
elif g == "*":
    result = a * t
elif g == "/":
    result = a / t
else:
    print("error")

print(a, g ,t," = ", result)

