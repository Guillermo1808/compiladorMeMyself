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
    
    def top(self):
        return self.stack[-1]
    
    def empty(self):
        if len(self.stack) > 0:
            return False
        else:
            return True
    
    def size(self):
        return len(self.stack)
    
# if __name__ == "__main__":
#     POper = stacks()
#     PIper = stacks()
#     POper.add('x')
#     em = POper.empty()
#     print(em)
#     em = PIper.empty()
#     print(em)