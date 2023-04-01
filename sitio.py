#Lorena Martins
n = int(input())

for i in range(n):
    x = int(input())
    y = int(input())
    
    if x < 1 or x > 500:
        break 
    elif y < 2*x or y > 4*x or y % 2 != 0:
        break 
    else:
        galinha = (4*x - y)//2
        carneiro = x - galinha
        print(f"{galinha} {carneiro}")