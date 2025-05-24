def organizarRegistrdos(registrados):
    resultado = ""
    for i in range(len(registrados)):
        resultado += str(registrados[i].nome) + ": " + str(registrados[i].infracoes) + ", "
    return resultado

class Sisae:
    def __init__(self):
        self._alunosRegistrados = []
    
    def adicionarRegistro(self, alunoDoMal):
        alunoDoMal.infracoes += 1
        if(not alunoDoMal in self._alunosRegistrados):
            self._alunosRegistrados.append(alunoDoMal)
    
    def imprimir(self):
        print(f'''
            Registrados: {organizarRegistrdos(self._alunosRegistrados)}
            ''')

    @property
    def alunosRegistrados(self):
        return self._alunosRegistrados
    @alunosRegistrados.setter
    def registros(self, novosRegistros):
        self._reg_alunosRegistradosistros = novosRegistros