idade = int(input("Digite a sua idade: "))

resposta = "S"

while resposta == "S":
    if idade < 16:
        print("não pode votar")

    elif idade == 16 or idade == 17:
        print("O voto é opcional")

    elif idade >= 18 and idade <= 70:
        print("O voto é obrigatorio")

    else:
        print("O voto é opcional")

    resposta = input("Deseja verificar outra idade digite (S/N) ? : ")