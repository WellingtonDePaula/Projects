class Pessoa():
    def __init__(self, nome: str, email: str, telefone: str):
        self.nome = nome
        self.email = email
        self.telefone = telefone
    
    def imprimirPessoa(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print()

def listarPessoas(lista: list):
    for pessoa in lista:
        pessoa.imprimirPessoa()


def verificarInputValido(answer):
    while(True):
        try:
            answer = int(answer)
            if(answer >= 1 and answer <= 3):
                return True
            print("Digite uma opção válida")
            return False
        except ValueError:
            print("Input inválido")
            return False

def main():
    pessoas = []
    while(True):
        print("----------Menu----------")
        print("1- Listar pessoas")
        print("2- Cadastrar pessoa")
        print("3- Sair")

        while(True):
            answer = input("\n--> ")
            if(verificarInputValido(answer)):
                answer = int(answer)
                break

        if(answer == 1):
            listarPessoas(pessoas)
        elif(answer == 2):
            nome = input("Digite o nome da pessoa a ser cadastrada:\n--> ")
            email = input("Digite o email da pessoa a ser cadastrada:\n--> ")
            telefone = input("Digite o telefone da pessoa a ser cadastrada:\n--> ")
            pessoas.append(Pessoa(nome, email, telefone))
        elif(answer == 3):
            print("Já vai ir?")
            break

main()