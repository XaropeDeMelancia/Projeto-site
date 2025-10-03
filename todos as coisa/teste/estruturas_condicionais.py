MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
idade = int(input("Informe sua idade:")) 

if idade >= MAIOR_IDADE:
        print("Maior de idade, pode tirar CNH")

if idade <= MAIOR_IDADE:
        print("Ainda nao pode tirar a CNH")


if idade >= MAIOR_IDADE:
        print("Maior de idade, pode tirar CNH")
        
else: 
    print("Ainda nao pode tirar a CNH")

if idade >= MAIOR_IDADE:
     print("Maior de idade, pode tirar CNH")

elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas, mas nao pode fazer aulas praticas.")
else: 
    print("Ainda nao pode tirar a CNH.")