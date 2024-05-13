'''matriz = [[1,2,3,],
          [4,5,6],
          [7,8,9],
          [1,1,1]]

for i in range (len(matriz)):
    for j in range (len(matriz[0])):
        print(matriz[i][j])'''
          

alunos = [
    [ "FELIPE","LUIS FELIPE",  ""       , "ADRIEL"],    
    [ "PEDRO" ,   "HIGOR"   ,   "GIL"   ,"MAYANARA"],    
    [    ""   , "ADRIAN" ,"LUIS CARLOS" ,"LUIZ GUSTAVO"],   
    [   ""    , "GABRIEL"  ,    ""      , "ARTHUR"],    
    [    ""   ,      ""    ,"ANDERSON"  , ""]]    

for i in range(len(alunos)):
    for j in range (len(alunos[0])):
        print(alunos[i][j])
    print("--------")

'''
matriz = [[0,0,0,],
          [0,0,0],
          [0,0,0],
          [0,0,0]]

i = 0
j = 0
maior_10= 0
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = int(input(f"Digite os valores:[{i}][{j}]:"))
        if( matriz[i][j]>10):
            maior_10 += 1

print("Foram",maior_10," numeros maior que 10")'''

matriz = [[0,0,0,],
          [0,0,0],
          [0,0,0],
          [0,0,0]]

linha = 0
coluna= 0
maior= 0
menor = 0
for i in range(len(matriz)): #linha
    for j in range(len(matriz[0])): #coluna
        matriz[i][j] = int(input(f"Digite os valores:[{i}][{j}]:"))
        if(matriz[i][j] >maior):
            maior = matriz[i][j]
            linha = i
            coluna = i
        else:
            (matriz[i][j]< menor)
            menor = matriz[i][j]
            linha = i
            coluna = i
          

print("O número maior foi",maior,"no posição",linha,)
print("O número menor foi",menor,"no posição",coluna)
'''
matriz_2 =[[0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0]]
#matriz na posição i e j recebe 1

for i in range (matriz_2(0,5)):
   matriz_2
   '''
       
       
