from turma import Turma
from sisae import Sisae

def organizarTurmas(turmas):
    resultado = ""
    for i in range(len(turmas)):
        resultado += str(turmas[i]._id) + ", "
    return resultado

class Escola:
    def __init__(self, nome):
        self._nome = nome
        self._sisae = Sisae()
        self._turmas = []
    
    def cadastrarTurma(self, turmaId):
        novaTurma = Turma(turmaId, self)
        self._turmas.append(novaTurma)
    
    def organizarTurmas(self):
        resultado = ""
        turmas = self._turmas
        for i in range(len(turmas)):
            resultado += str(turmas[i]._id) + ", "
        return resultado
    
    def imprimir(self):
        print(f'''
            Nome: {self._nome}
            Turmas: {self.organizarTurmas()}
            ''')

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novoNome):
        self._nome = novoNome
        
    @property
    def turmas(self):
        return self._turmas
    @turmas.setter
    def turmas(self, novasTurmas):
        self._turmas = novasTurmas
    
    @property
    def sisae(self):
        return self._sisae