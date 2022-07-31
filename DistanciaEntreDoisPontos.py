import math

x1 = float(input('Informe o valor do eixo x 1: '));

y1 = float(input('Informe o valor do eixo y 1: '));

x2 = float(input('Informe o valor do eixo x 2: '));

y2 = float(input('Informe o valor do eixo y 2: '));


calcDistancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2);

print(f'{calcDistancia:.4f}');