def lista_random(lista):
    for i in range(0,10000):
        lista.append(random.randint(0,10000))
        
def bubble_sort(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]

def quick_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quick_sort(lista, inicio, p-1)
        quick_sort(lista, p+1, fim)

def partition(lista, inicio, fim):
    pivot = lista[inicio]
    i = inicio + 1
    while True:

        while i <= fim and lista[fim] >= pivot:
            fim = fim - 1
        
        while i <= fim and lista[i] <= pivot:
            i = i + 1
        
        if i <= fim:
            lista[i], lista[fim] = lista[fim], lista[i]
        else:
            break
    lista[inicio], lista[fim] = lista[fim], lista[inicio]
    return fim


import random, time

listaElem = []

print('Ordenando, aguarde...')
lista_random(listaElem)
iniciob = time.time()
bubble_sort(listaElem)
fimb = time.time()

lista_random(listaElem)
inicioq = time.time()
quick_sort(listaElem)
fimq = time.time()

#print('\nLista ordenada BubbleSort:', listaElem)
#print('\nLista ordenada QuickSort:', listaElem) 

print('\nTempo gasto BubbleSort:', ((fimb - iniciob)*1000),'ms \nTempo gasto QuickSort: ', (fimq - inicioq)*1000,'ms')