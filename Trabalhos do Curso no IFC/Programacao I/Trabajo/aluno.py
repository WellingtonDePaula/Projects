class Aluno:
    def __init__(self, nome):
        self._matricula = 0
        self._nome = nome
        self._infracoes = 0
    
    def imprimir(self):
        print(f'''
            Matrícula: {self._matricula}
            Nome: {self._nome}
            ''')

    @property
    def matricula(self):
        return self._matricula
    @matricula.setter
    def matricula(self, novaMatricula):
        self._matricula = novaMatricula

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novoNome):
        self._nome = novoNome

    @property
    def infracoes(self):
        return self._infracoes
    @infracoes.setter
    def infracoes(self, novaInfracao):
        self._infracoes = novaInfracao