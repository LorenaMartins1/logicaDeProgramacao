op= "A"
while op != "F":
    op=input("""Digite um caracterere
    A = Ateração
    C = Consulta
    E = Exclusão
    I = Inclusão
    F = Finalizar \n""")

    if op == "A" or  op == "a":
        print("Ateração")
    elif op == "C" or op == "c":
        print("Consulta")
    elif op == "E" or op == "e":
        print("Exclusão")
    elif op == "I" or op == "i":
        print("inclusão")
    elif op == "F" or op == "f":
        print("Finalizou")
    else:
        print("opção inválida!")

