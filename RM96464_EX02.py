votos_segunda=int(input("insira a quantidade de votos para segunda: "))
votos_terca=int(input("insira a quantidade de votos para terca: "))
votos_quarta=int(input("insira a quantidade de votos para quarta:  "))
votos_quinta=int(input("insira a quantidade de votos para quinta: "))
votos_sexta=int(input("insira a quantidade de votos para sexta: "))
votos= [votos_segunda,votos_terca,votos_quarta,votos_quinta, votos_sexta]
max_value = None

for num in votos:
    if (max_value is None or num > max_value):
        max_value = num

print('O dia com mais votos obteve {} votos e portanto esse dia deverá ser escolhido'.format(max_value))