class Pessoa:
    def __init__(self, nome, email, dt_nasc, cpf, senha):
        self.nome = nome
        self.email = email
        self.data_nascimento = dt_nasc
        self.cpf = cpf
        self.senha = senha

    def __str__(self):
        return f'''
        Nome: {self.nome}, 
        Email: {self.email}, 
        Nascido(a) em: {self.data_nascimento}'''