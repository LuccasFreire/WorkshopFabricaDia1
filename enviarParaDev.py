print("Este arquivo so foi criado para ser enviado para a nova branch criada Dev")
numb = 3
sucessor = str((lambda n1: n1 + 1)(numb))
antecessor = str((lambda n1: n1 - 1)(numb))

print("Sucessor: " + sucessor)
print("Antecessor: " + antecessor)