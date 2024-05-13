print("Alistamento do Exercicito precisamos de algumas informações ")
escolha = input("seu sexo M para Masculino e F para Feminino:")
Altura = float(input("agora digite sua altura em metros:"))

if escolha == ("M"):
    print("Para seu sexo Masculino, a altura que voce precisaria era igual ou superior a 1.70 metros ")
    if Altura>= 1.70:
        print("Você foi aprovado no alistamento!,Parabéns.")
    else :
        print("Você não foi aprovado,até mais!!")

elif escolha ==("F") :
    print("Para o sexo feminino, a altura que voce precisaria era igual ou superior a 1.60 metros")
    if Altura >= 1.60:
        print("Você foi aprovado no alistamento!!Parabéns.")
    else:
        print("você não foi aprovado no alistamento,até mais!!")
else :
    print("caracterer invalido")

print("Lição 2<<<<<<<>>>>>>>")

num_1 = int(input("digite um numero:")) 
num_2 = int(input("digite o segundo número:"))
num_3 = int(input("digite o terceiro número:"))

maior = num_1
if num_2 > num_1 and num_2 > num_3:
    maior = num_2
if num_3 > num_1 and num_3 >= num_2:
    maior = num_3
menor = num_1
if num_2 < num_3 and num_2 < num_1:
    menor= num_2
if num_3 <= num_2 and num_3 < num_1:
    menor = num_3

print("O menor numero digitado foi:",menor)
print("O maior numero digitado foi:",maior)


print("Lição 3<<<<<<>>>>>>>")

print("CONVERSOR DE TEMPERATURA 2024")

print("1- Celsius para Fahrenheit")
print("2- Fahrenheit para Celsius")

opção = int(input("escolha a conversão que deseja:"))

match opção:
    case 1:
         temperatura = float(input("informe a temperatura em celsius: "))
         print("o valor em fahrenheit é:", (temperatura * 9/5) + 32)

    case 2:
         temperatura = float(input("informe a temperatura em fahrenheit: "))
         print("o valor em celsius é:",(temperatura -32) * 5/9)




