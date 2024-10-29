from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def fazer_som(self): # tem que ter o self
        pass

class Gato(Animal):
    """ 
        Sem self, os métodos não teriam uma referência para acessar ou
        modificar os atributos da instância específica.
        
        Mesmo que self não seja usado diretamente na definição do método
        abstrato, ele é importante para a assinatura do método e para manter 
        a interface consistente quando implementado nas subclasses.

        Python automaticamente passa a instância como o primeiro argumento para 
        o método. 
        
        Sem self, o método não sabe como lidar com esse argumento 
        adicional.

        Caso não use o "self", retornará o seguinte erro:
        TypeError: fazer_som() takes 0 positional arguments but 1 was given
        - takes 0 positional (método sem o self não espera argumentos)
        - but 1 was given (Python passou o self por padrão)
    """
    def fazer_som(self):
        return "Miau"
    
class Cachorro(Animal):
    # self é usado para acessar atributos específicos do objeto, se necessário
    def fazer_som(self):
        return "Au"
    
gato = Gato() # cuidado para não colocar gato = new Gato()
cachorro = Cachorro()

print(gato.fazer_som())
print(cachorro.fazer_som())

# Can't instantiate abstract class Animal without an implementation for 
# abstract method 'fazer_som'
try:
    animal = Animal()
except Exception as e:
    print(e)