listPessoas = []
pessoas = {}

while True:
    pessoas.clear()
    pessoas['Nome'] = input("Digite o nome da pessoa: ")
    while True:
        pessoas['Sexo'] = input("Digite o sexo - M ou F': ").upper()[0]
        if pessoas['Sexo'] in 'MF':
            break
        print('ERRO!!, digite apenas M ou F')
    pessoas['Idade'] = int(input("Digite a idade: "))
    listPessoas.append(pessoas.copy())
    while True:
        resposta = input("Quer continuar? S ou N").upper()[0]
        if resposta in 'SN':
            break
        print('Erro! Responda apenas S ou N')
    if resposta == 'N':
        break
    
print(listPessoas)

# print(tabulate(table, headers=["Nome", "Sex o", "Idade"], tablefmt="grid"))

