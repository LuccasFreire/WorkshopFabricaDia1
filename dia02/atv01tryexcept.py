
number: int = input("Insert the number: ")

antecessor = 0
sucessor = 0

try:
    sucessor = int(number) + 1
    antecessor = int(number) - 1
except ValueError:
    raise ValueError("Digite um numero")

print(f"Antecessor: {antecessor} \n Sucessor: {sucessor}" )