'''cont =0
while cont <= 10:
    print(cont)
    cont += 1

not_1 = float(input("Digite uma nota:"))
while not_1 <0 or not_1 >10:
    not_1 = float(input("digite a senha novamente"))

not_2 = float(input("Digite a segunda nota:"))
while not_2 <0 or not_2 >10:
    not_2 = float(input("digite a senha novamente"))

print(not_1)
print(not_2)


login = input("Informe o login:")
senha = input(("Informe a senha:"))
while senha == login:
    print("Senha incorreta")
    senha = input("informe a senha novamente:")

print("Valido")


nome =input("DIGITE SEU NOME:")

while len(nome)<2:
    print("Nome invalido")
    nome = input("Digite seu nome novamente:")

print("NOME VALIDO!!")


idade = int(input("Qual sua idade:"))

while idade <0 or idade > 120:
    print("Idade incorreta!Por favor digite novamente")
    idade = int(input("Digite sua idade novamente:"))

print("Manero!sua idade esta correta")

Salário = float(input("Qual o seu salario na folha de pagamento:"))

while Salário <0:
    print("Incorreto!")
    Salário = float(input("Digite seu salario novamente:"))

print("Boa,Seu salario é correto")

Gênero = input("Informe seu sexo M para masculino e F para feminino:")

while Gênero != "M" and Gênero != "F":
    print("Sexo Invalido!")
    Gênero = input("Digite seu sexo novamente:")

print("Sexo correto")

estado_civil = input("Qual seu estado civil S para solteiro C para Casado V para Víuvo(a) e D para Divorciado:")
while estado_civil != "S" and estado_civil != "C" and estado_civil != "V" and estado_civil != "D":
    print("Estado civil incorreto")
    estado_civil = input("Digite seu estado civil novamente:")

print("Verídico")'''

tabuada = int(input("Informe o número para a tabuada:"))

for i in range(1,11):   
    print(i,"x", tabuada, "=", (i * tabuada))














