# as estruturas de repetição avaliam uma condição,Se verdadeiro é iniciada a repetição.
# A avaliação da condição é feita a cada iteração("nova execução" do loop)
# O loop só termina quando a condião de avaliação é falsa

# Faça <passo> em<sequencia>:
     #<instruções>

Lista = [1,2,3,4,5]

print(Lista[2])

print("<<<<>>>>")

for i in Lista:
    print(i)

frutas = ["maça","uva","pera","goiaba","mamão"]

for i in frutas:
    print(i)

for i in range(0,5,2):
    print(frutas[i])

range(0,5,2) # "0"onde comeca,  "5" onde termina;  "2"aumento em dois em dois a lista 

for i in range(2,21,2):
    print(i)


maior_10 = 0
for i in range(5):
    num = int(input("Informe o valor:"))
    if(num>10):
        maior_10 +=1



print("os numeros maior que 10 são;",maior_10)

n = int(input("diga um valor para o fatorial:"))
fatorial = n
for i in range(n-1,1,-1):
    fatorial = fatorial *i

print(fatorial)
    



            


