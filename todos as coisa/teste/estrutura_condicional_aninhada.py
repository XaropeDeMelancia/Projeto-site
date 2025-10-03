conta_normal = False
conta_uiversitaria = False

saldo = 2000 
saque = 2500 
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com suecesso!")
    elif saque <= (saldo + cheque_especial):
        print("saque realizado com uso do cheque especial!")
    else:
        print("Nao foi possivel realiozar o saque, saldo insuficiente ")
elif conta_uiversitaria:
    if saldo >= saque:
        print("Saque realziado com sucesso")
    else:
        print("Saldo insuficiente")