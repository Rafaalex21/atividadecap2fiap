faturamento_anual = float(input("Digite o faturamento anual em R$:"))
print("planos: basic(1), silver(2), gold(3), platinum(4)")
assinatura = int(input("Qual o seu plano de assinatura?: "))
if(assinatura) == 1:
    bonus= float(faturamento_anual * 0.3)
    print("o bônus a pagar será de R$ {}".format(bonus))
elif(assinatura) == 2:
    bonus= float(faturamento_anual * 0.2)
    print("o bônus a pagar será de R$ {}".format(bonus))
elif(assinatura) == 3:
    bonus= float(faturamento_anual * 0.1)
    print("o bônus a pagar será de R$ {}".format(bonus))
elif(assinatura) == 4:
    bonus= float(faturamento_anual * 0.05)
    print("o bônus a pagar será de R$ {}".format(bonus))

