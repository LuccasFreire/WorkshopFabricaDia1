
age = input(("Por favor insira sua idade: "))

try:
    if int(age) <= 0:
        print("Digite uma idade valida!")
    elif int(age) >= 18:
        print("Voce pode tirar CNH")
    else:
        print("Voce não tem a idade necessaria para tirar a cnh")
except ValueError:
    raise ValueError("Digite um numero! Letras ou caracteres especiais nao sao permitidos")