media = int(input("Digite sua média: "))

if media >= 9:
    print("A")
elif media >= 8 and media < 9:
    print("B")
elif media >= 7 and media < 8:
    print("C")
elif media >= 5 and media < 7:
    print("D")
elif media < 5:
    print("E")