n = int(input("Digite o número do funcionãrio: "))

if n >= 100:
    v1 = float(input("Digite o valor anual do funcionário: "))
    pagSema = v1/52
    print(pagSema)
if n < 40:
    v1 = float(input("Digite as horas trabalhadas: "))
    preco =  float(input("Digite o valor pago por hora:"))
    pagHora = v1 * preco
    print(f"Salário: {pagHora}")
if n >= 40 and n < 100:
    pagHora = (v1 * preco) 
    porcento = pagHora * 0.5
    pagHora = (v1 * preco) + porcento
    print(f"Salário: {pagHora}")
        




