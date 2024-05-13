'''vetor = ["Maynara","Luis Carlos","Luis gustavo","Arthur","Andernson","Gabriel","luana","Adrian","Anderson","Higor","Pedro","Luis Felipe","Felipe"]

print(vetor)

print(vetor[7],"Chegou atrasado")


cont = 0
for i in vetor:
    if i[0]== "A":
        cont += 1
    
print(cont)'''


A= [0,0,0,0,0]

for i in range(len(A),0,-1):
    A[i-1]= int(input("Digite um valor:"))
   

print(A)