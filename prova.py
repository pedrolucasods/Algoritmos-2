import os

##### Funções auxiliares
def exibir_dados(objeto):
    for key,value in objeto.items():
        print(f"{key}: {value}")

def exibir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"[{matriz[i][j]}]", end=" ")
        print()

## Exercicio 01
# latencia = [float(input(f"Informe o valor do dia {i+1}º: ")) for i in range(7)]

# def analisar_latencia(lista):
#     media = (sum(lista))/len(lista)
#     qtd_acima = 0
#     for valor in lista:
#         if(valor>media):
#             qtd_acima+=1

#     dados = {
#         "Media":media,
#         "Quantidade de dia acima da média":qtd_acima
#     }

#     return dados

# exibir_dados(analisar_latencia(latencia))



##### Exercicio 02 ###############################################################################
# empresas = [input("Informe o nome da empresa: ") for i in range(4)]
# os.system("cls")
# matriz = []
# for i in range(4):
#     linha = []
#     for j in range(3):
#         nota = float(input(f"Informe a nota a empresa {empresas[i]}: "))
#         linha.append(nota)
#     matriz.append(linha)

# os.system('cls')
# nota_corte = float(input("Informe a nota corte: "))

# def auditoria(empresas,matriz,nota_corte):
#     empresas_maior_seguranca = []
#     for i in range(len(matriz)):
#         for j in range(len(matriz[i])):
#             if(j == 1):
#                 if(matriz[i][j] >= nota_corte):
#                     empresas_maior_seguranca.append(empresas[i])

#     matriz_correcao = []
#     for i in range(len(matriz)):
#         linha = []
#         for j in range(len(matriz[i])):
#             if(matriz[i][j] < 5):
#                 linha.append(5)
#             else:
#                 linha.append(matriz[i][j])
#         matriz_correcao.append(linha)

#     return empresas_maior_seguranca,matriz_correcao

# empresas_seguras, matriz_correcao = auditoria(empresas,matriz,nota_corte)

# exibir_matriz(matriz)
# print(f"Empresas maior segurança da nota corte: {empresas_seguras}")
# print("\nMatriz corrigida: ")
# exibir_matriz(matriz_correcao)


##### Exercicio 03 ############################################################################
lista_inteiros = [1,2,3,4,5,6,7,8,9,10]
def fatiamento_exericico(lista):
    dados={
        "Primeiros 5 números":lista[4::-1][::-1],
        "Ultimos 5 números":lista[-5::],
        "Meio até o indice 5":lista[4::-1][1::-1]
    }

    return dados
exibir_dados(fatiamento_exericico(lista_inteiros))

