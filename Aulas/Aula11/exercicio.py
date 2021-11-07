#Definir exceptions

class UsernameDuplicado(Exception):
    pass

class IdadeMenor(Exception):
    pass

class IdadeInvalida(Exception):
    pass

class EmailInvalido(Exception):
    pass

class User:
    def __init__(self, username, idade, email):
        self.__username = username
        self.__idade = idade
        self.__email = email

    def getUserName(self):
        return self.__username

    def getIdade(self):
        return self.__idade
    
    def getEmail(self):
        return self.__email
    
if __name__ == "__main__":

    listaExemplo = [
        ("paulo", "paulo@gmail.com", 21), 
        ("maria", "maria@gmail.com", 19), 
        ("antonio", "antonio@gmail.com", 25), 
        ("pedro", "pedro@gmai.com", 15), 
        ("marisa", "marisa", 23),
        ("ana", "ana@gmail.com", -22), 
        ("maria", "maria@gmail.com", 27)
    ]
    
    cadastro = {}

    for username, email, idade in listaExemplo:
        
        try:
            if username in cadastro:
                raise UsernameDuplicado()
            if idade < 0:
                raise IdadeInvalida()
            if idade < 18:
                raise IdadeMenor()
            emailpartes = email.split('@')
            if len(emailpartes) != 2 or not emailpartes[0] or not emailpartes[1]:
                raise EmailInvalido()
            else:
                cadastro[username] = User(username, idade, email)

        except UsernameDuplicado:
            print("Username %s ja está em uso" % username)

        except IdadeInvalida:
            print("Idade inválida: %d" % idade)
        
        except IdadeMenor:
            print("Usuario %s tem idade inferior a permitida" % username)
        
        except EmailInvalido:
            print("%s não é um endereço de email válido" % email)
        

