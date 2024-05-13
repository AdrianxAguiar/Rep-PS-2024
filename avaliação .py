'''matriz = [0,0,0,0,0,] #i
          

linha = 0
maior = 0
menor = 0
indice = 0
for i in range(len(matriz)):
     matriz[i] = int(input(f"Digite os valores:[{i}]:"))
     if matriz[i] > maior:
        maior = matriz[i]
        indice = i
     if matriz[i] < matriz[linha]:#menor que 0
        linha = i
        
    
print("maior número esta na posição",indice)
print("menor número esta na posiçãO",linha)       
'''

print("lição 2<<<<<<<<>>>>>>>>")

vetor_1 = [0,0,0,0,0]
vetor_2 = [0,0,0,0,0]


aux= 0

vetor_3 =[]
for i in range(len(vetor_1)):
    vetor_1[i] =int(input("Digite os valores do vetor 1:"))
    vetor_2[i] =int(input("Digite os valores do vetor 2:"))
    if vetor_1 == vetor_2:
        aux +=1 
        vetor_3 = aux
    
print(vetor_1)
print(vetor_2)
print(vetor_3)
   

