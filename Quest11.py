a=int(input("Digite o valor a: "))
b=int(input("Digite o valor b: "))
c=int(input("Digite o valor c: "))

d = (b**2 - 4*a*c)
x1 = (-b + d**(1/2)) / (2*a)
x2 = (-b - d**(1/2)) / (2*a)

print(f"Valor de x1: {x1}")
print(f"Valor de x2: {x2}")

