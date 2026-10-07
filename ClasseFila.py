class Fila:
    
    def __init__(self):
        self._pacientes = []

    def entrar(self, paciente):
        self._pacientes.append(paciente)

    def chamar(self):
        if not self.isEmpty():
            return self._pacientes.pop(0)
        return None
    
    def size(self):
        return len(self._pacientes)
    
    def isEmpty(self):
        return len(self._pacientes) == 0
    
    def proximo(self):
        if not self.isEmpty():
            return self._pacientes[0]
        return None
    
    def verFila(self):
        print(self._pacientes)