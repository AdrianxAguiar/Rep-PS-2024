'''numero_1 = float(input("Digite um número:"))
numero_2 = float(input("Digite o segundo número:"))

if numero_1 > numero_2:
    print("O numero",numero_1,"é maior que o",numero_2,)
elif numero_1 == numero_2:
    print("OS numeros são iguais")
else:
    print("O numero",numero_2,"é maior que o",numero_1,)'''



'''num_ = float(input("Digite um número:"))

if num_<0:
    print("O valor é negativo")
else:
    print("o valor é positivo")'''

'''Gênero = input("Informe seu sexo:")

if Gênero == "M":
    print("Seu gênero é masculino")
elif Gênero == "F" :
        print("Seu gênero é Feminino")
else:
      print("Erro")'''

'''num_1 = int(input("digite um numero:"))
num_2 = int(input("digite o segundo numero:"))
num_3 = int(input("digite o terceiro numero:"))

if num_1 > num_2 and num_1 >num_3:
    print(num_1)
elif num_2 > num_1 and num_2 > num_3:
    print(num_2)
else:
    print(num_3)'''

print("Intimação 002;Algumas perguntas deve responder sim ou não")

a = input("Telefonou para a vitima?")
b= input("Esteve no local do crime?")
c = input("Mora perto da vítima?")
d = input("Devia para a vítima?")
e = input("Já trabalhou com a vítima?")

contador_1 = 0


if a == "sim" or "não":
    print(contador_1)
    contador_1 = contador_1 +1
elif b == "sim" or "não":
    print(contador_1)
    contador_1 = contador_1 +1
elif c == "sim" or "não":
    print(contador_1)
    contador_1 = contador_1 +1
elif d == "sim" or "não":
    print(contador_1)
    contador_1 = contador_1 +1
elif e == "sim" or "não":
    print(contador_1)
    contador_1 = contador_1 +1
    if contador_1 >= 2:
        print("Suspeito")
    elif contador_1 >= 3 and 4:
        print("Cúmplice")
    else:
        print("Assasino(a)")


   




