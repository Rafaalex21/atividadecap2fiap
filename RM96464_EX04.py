minuto = int(input("Qual minuto a maquina está marcando no momento ?"))
total = 1
for n in range(minuto):
    total = total * (n + 1)


print("a senha será LIBERDADE{}".format(total))