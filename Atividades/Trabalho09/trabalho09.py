Estoque = {} #Dicionário estoque

#Exceptions
class ProdutoInvalido(Exception):
    pass

class SemEstoque(Exception):
    pass

class Produto():
    def __init__(self, codigo, descricao, valorUnitario):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valorUnitario = valorUnitario
    
    def getCodigo(self): #Identifica cada produto
        return self.__codigo

    def getDescricao(self): #Descreve cada produto
        return self.__descricao

    def getValorUnitario(self): #Preço de cada produto 
        return self.__valorUnitario
    
class NotaFiscal():
    def __init__(self, nroNF, nomeCliente, itensNF):
        self.__nroNF = nroNF
        self.__nomeCliente = nomeCliente
        itensNota = list(itensNF) 
        self.__itensNF = itensNota
        contItem = 0 #contador de itens
        contErro = 0 #contador de erros

        for item in itensNota:
            contItem+=1 
            try:
                if item[0].getCodigo() not in Estoque:
                    raise ProdutoInvalido()
                if Estoque[item[0].getCodigo()] < item[1]:
                    raise SemEstoque()
            except ProdutoInvalido:
                print('Produto Nº%d não existente' % item[0].getCodigo())
                itensNota.pop() #Remove item da nota fiscal
                contErro+=1
            except SemEstoque:
                print('Produto Nº%d faltou no estoque' %  item[0].getCodigo())
                contErro+=1
            else:
                Estoque[item[0].getCodigo()] = Estoque[item[0].getCodigo()] - 1
                
        if contErro == 0:
            print('Nota fiscal criada com sucesso')
        elif contErro >= contItem:
            print('Nota fiscal não criada')
        else:
            print('Nota fiscal criada parcialmente')

    def getNroNF(self):
        return self.__nroNF

    def getNomeCliente(self):
        return self.__nomeCliente

    def getItensNF(self):
        return self.__itensNF


if __name__ == "__main__":
    listaProdutos = [
        Produto(100, 'Camiseta QuickSilver', 70),
        Produto(120, 'Camisa polo Wear', 100),
        Produto(130, 'Calça moletom Fatal Surf', 90),
        Produto(200, 'Calça jeans Levis', 95),
        Produto(220, 'Sapato social Vizzano', 120),
        Produto(230, 'Tênis cano curto Nike SB', 250)
    ]
    #Definição do estoque de produtos
    Estoque[listaProdutos[0].getCodigo()] = 2
    Estoque[listaProdutos[1].getCodigo()] = 1 
    Estoque[listaProdutos[2].getCodigo()] = 2 
    Estoque[listaProdutos[3].getCodigo()] = 5 
    Estoque[listaProdutos[4].getCodigo()] = 2 
    Estoque[listaProdutos[5].getCodigo()] = 3 

    itensNota = (
        (Produto(100, 'Camiseta QuickSilver', 70), 2),
        (Produto(120, 'Camisa polo Wear', 100), 1),
        (Produto(130, 'Calça moletom Fatal Surf', 90), 2),
        (Produto(230, 'Tênis cano curto Nike SB', 250), 1),
        (Produto(150, 'Chinelo Havaianas', 40), 1) #código não existente
    )
    Nf = NotaFiscal(20192020, 'User', itensNota)

    print("======== Nota Fiscal ========")
    print("Número da Nota: %d" % Nf.getNroNF())
    print("Cliente: %s" % Nf.getNomeCliente())
    print("---------itens-----------")
    items = Nf.getItensNF()
    for item in items:
        print('Produto: %s' % item[0].getDescricao())
        print('Preço Unitário: R$%d' % item[0].getValorUnitario())
        print('Vendidos: %s' % item[1])
        print('----------------------------')
