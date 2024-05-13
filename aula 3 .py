'''dia = int(input("Informe o dia da semana:"))

match dia:
    case 1:
        print("Segunda feira")
    case 2:
        print("Terça feira")
    case 3:
        print("Quarta feira")
    case 4:
        print("Quinta feira")
    case 5:
        print("Sexta feira")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")'''


'''Gênero = input("Informe seu sexo:").upper()

#lower()   #transforma todo o texto em minusculo
#upper()   #Transforma todo otexto em maiusculo

match Gênero:
    case "F":
        print("Sexo Feminino")
    case "M":
        print("Sexo Masculino")
    case _:
        print("Sexo não definido")'''

'''print("Olá usúario bem vindo ao sistema de atendimento!!")
print("1-Fazer Check-in 2- Chamar serviço de quarto 3- Fazer pedido 4- Fazer Check-out")

Serviço =int(input("Escolha uma das opções do Menu:"))

match Serviço:
    case 1:
        print("Check-in realizado com sucesso!")
    case 2:
        print("Serviço de quarto disponibilizado!")
    case 3:
        print("Seu pedido foi realizado!")
    case 4:
        print("Check-out foi realizado!")
    case _:
        print("Digite novamente;as opções corretas")'''


'''valor_1 = int(input("Digite um número:"))
valor_2 = int(input("Digite o segundo número"))

Operação = input("Qual operação quer execultar soma +,subtração -, multiplicação *, divisão /:")

match Operação:
    case "+":
        print("o resultado da sua operação é:",valor_1+ valor_2)
    case "-":
        print("o resultado da sua operação é",valor_1-valor_2)
    case "*":
        print("O resultado da sua operação é",valor_1 * valor_2)
    case "/":
        print("O resultado da sua operação é",valor_1 / valor_2)
    case _:
        print("Erro")'''


num_1 = int(input("digite o primeiro número:"))
num_2 = int(input("digite o segundo número:"))
num_3 = int(input("digite o terceiro numero:"))


if num_1 > num_2:
    temp = num_1
    num_1 = num_2
    num_2 = temp
if num_2 > num_3:
    temp = num_2
    num_2 = num_3
    num_3 = temp
if num_1 > num_2:
    temp = num_1
    num_1 = num_2
    num_2 = temp
print(num_1,num_2,num_3)
        


