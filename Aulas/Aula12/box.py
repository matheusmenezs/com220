from abc import ABC, abstractmethod

class Item:
    def __init__(self, name, value):
        self.__name = name
        self.__value = value

    def getName(self):
        return self.__name

    def getValue(self):
        return self.__value
    
class Box(ABC):

    @abstractmethod
    def add(self, item): #adiciona item na caixa
        pass

    @abstractmethod
    def empty(self): #esvazia a caixa e retorna os itens da caixa
        pass
        
    @abstractmethod
    def count(self): #conta os itens da caixa
        pass

class ListBox(Box):
    def __init__(self):
        self.__items = [] #lista vazia
    
    def add(self, item):
        self.__items.append(item)

    def empty(self):
        items = self.__items #armazena conteudo da lista
        self.__items = [] #retira conteudo da lista
        return items 
    
    def count(self):
        return len(self.__items)

class DictBox(Box):
    def __init__(self):
        self.__items = {} #dicionario vazio

    def add(self, item):
        if item.getName() in self.__items: #verifica se o nome ja foi inserido
            chave = item.getName() + item.getName() #gerar uma chave diferente, composição dos nomes
        else:
            chave = item.getName()
        self.__items[chave] = item
    
    def empty(self):
        items = list(self.__items.values()) #values: func. para dicionario, acessa os valores
        self.__items = {}
        return items

    def count(self):
        return len(self.__items)

def repackBoxes(*boxes): #armazena as 3 caixas em uma lista (lista de parametros)
    items = []

    for box in boxes:
        items.extend(box.empty()) #extend: junta lista de items / box.empty retorna lista de itens
    
    while items: #pega todos os itens
        for box in boxes: 
            try: 
                box.add(items.pop()) #tira um item da lista e adiciona na caixa
            except IndexError:
                break

if __name__ == "__main__":

    box1 = ListBox()
    for i in range (20):
        box1.add(Item(str(i), i))

    box2 = ListBox()
    for i in range (9):
        box2.add(Item(str(i), i))

    box3 = DictBox()
    for i in range (5):
        box3.add(Item(str(i), i))

repackBoxes(box1, box2, box3)

print(box1.count())
print(box2.count())
print(box3.count())
