#  Merge de Listas Ordenadas: Desenvolva uma função que receba duas listas que já
# estão ordenadas de forma crescente. A função deve retornar uma única lista contendo
# todos os elementos de ambas, também ordenada. Não é permitido concatenar e aplicar
# algoritmo de ordenação depois.

def merge_lista(lista_1,lista_2):
    lista_mergeada = []
    soma_tamanho = len(lista_1)+len(lista_2)
    while len(lista_mergeada)!=soma_tamanho-2:
        menor_l1 = menor_numero_da_lista(lista_1)
        menor_l2 = menor_numero_da_lista(lista_2)
        if(menor_l1<menor_l2):
            lista_mergeada.append(menor_l1)
            lista_1.remove(menor_l1)
        else:
            lista_mergeada.append(menor_l2)
            lista_2.remove(menor_l2)
    if(lista_1<lista_2):
        lista_mergeada.extend(lista_1)
        lista_mergeada.extend(lista_2)
    else:
        lista_mergeada.extend(lista_2)
        lista_mergeada.extend(lista_1)

    return lista_mergeada
        
def menor_numero_da_lista(lista):
    if(len(lista) == 1):
        return lista[0]
    else:
        menor = lista[0]
        for i in range(len(lista)):
            if(i == 0):
                pass
            else:
                if(lista[i]<menor):
                    menor = lista[i]
                else:
                    pass
        return menor


lista_b = [1,6,9,5,10,3]
lista_a = [1,6,9,5,10]
print(merge_lista(lista_a,lista_b))