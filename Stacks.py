# Guillermo Enrique Valles Villegas
# A01561722
# Clase para crear las listas que se usaran para la pila de Operaciones y Saltos

class stacks:

    def __init__(self) :
        self.stack = []
    
    def pop(self):
        return self.stack.pop()
        
    def add(self, item):
        self.stack.append(item)
        
    def clear(self):
        self.stack.clear()
    
    def print(self):
        print(self.stack)
    
if __name__ == "__main__":
    POper = stacks()
    POper.add('int')
    var = POper.pop()
    print(var)