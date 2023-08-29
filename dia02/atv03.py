
velo = input("Digite a velocidade do carro: ") #PEGANDO O VALOR EM STRING

veloemfloat = 0.0
acima = 0.0

try:
    veloemfloat = float(velo) #FAZENDO TRATAMENTO DE EXCESSAO E CONVERTENDO PARA FLOAT
except ValueError:
    raise ValueError("Digite um numero valido!")


if veloemfloat > 80.0:

    acima = veloemfloat - 80
    valordamulta = 7.0 * acima

    print(f"Voce passou do limite do radar em {acima:.2f} kmh")
    print(f"O valor a ser pago será de R$ {valordamulta:.2f}")
else:
    print("Voce não ultrapassou os limites de velocidade!")