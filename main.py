import math
#solicitando valores de A, B e C
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
#calculo do delta
delta = (b * b) - (4 * a * c)
#verificacao das condicoes
if delta > 0.0:
    #calculo de 2 valores para x
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Para a equacao {}x² + {}x + {} = 0, obtivemos os seguintes valores: x1 = {:.2f} e x2 = {:.2f}".format(a,b,c,x1,x2))
elif delta == 0.0:
    # calculo de 1 valor para x
    x = (-b + math.sqrt(delta)) / (2 * a)
    print("Para a equacao {}x² + {}x + {} = 0, obtivemos o seguinte valor: x = {:.2f}".format(a,b,c,x))
else:
    #nenhum calculo para x
    print("Nenhum valor real possivel para x na equacao {}x² + {}x + {} = 0".format(a,b,c))


