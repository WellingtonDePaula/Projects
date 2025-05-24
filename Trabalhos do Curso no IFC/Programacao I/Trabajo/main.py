from aluno import Aluno
from escola import Escola

escola1 = Escola("E.E.B. Bruno Hoeltgebaum")
escola1.cadastrarTurma("202")

sisae = escola1.sisae
turma1 = escola1.turmas[0]
aluno1 = Aluno("Wellington")
aluno2 = Aluno("Sofia")
aluno3 = Aluno("Ana")

turma1.adicionarAluno(aluno1)
turma1.adicionarAluno(aluno2)
turma1.adicionarAluno(aluno3)

sisae.adicionarRegistro(aluno2)
sisae.adicionarRegistro(aluno3)
sisae.adicionarRegistro(aluno3)


print("ALUNOS:")
aluno1.imprimir()
aluno2.imprimir()
aluno3.imprimir()
print("------------------------------------------------------")

print("TURMA:")
turma1.imprimir()
print("------------------------------------------------------")

print("SISAE:")
escola1.sisae.imprimir()
print("------------------------------------------------------")

print("ESCOLA:")
escola1.imprimir()
print("------------------------------------------------------")