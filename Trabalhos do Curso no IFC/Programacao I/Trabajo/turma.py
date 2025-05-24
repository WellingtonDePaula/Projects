from datetime import datetime
def gerarMatricula(turma):
    now = datetime.now()
    ano = str(now.year)
    mes = ""
    dia = ""
    if(now.month <= 9):
        mes += "0" + str(now.month)
    else:
        mes = str(now.month)

    if(now.day <= 9):
        dia += "0" + str(now.day)
    else:
        dia = str(now.day)

    alunoIndex = str(len(turma.alunos))
    matricula = ano + mes + dia + alunoIndex + "-" + turma.id
    return matricula

class Turma():
    def __init__(self, id, escola):
        self._id = id
        self._escola = escola
        self._alunos = []
    
    def adicionarAluno(self, novoAluno):
        novoAluno.matricula = gerarMatricula(self)
        self._alunos.append(novoAluno)

    def organizarAlunos(self):
        resultado = ""
        alunos = self._alunos
        for i in range(len(alunos)):
            resultado += str(alunos[i]._nome) + ", "
        return resultado
    
    def imprimir(self):
        print(f'''
            Id: {self._id}
            Escola: {self._escola.nome}
            Alunos: {self.organizarAlunos()}
            ''')

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, novoId):
        self._id = novoId
    
    @property
    def alunos(self):
        return self._alunos
    @alunos.setter
    def alunos(self, novosAlunos):
        self._alunos = novosAlunos