from pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome, email, dt_nasc, cpf, senha, telefone, tps):
        super().__init__(nome, email, dt_nasc, cpf, senha)
        self.telefone = telefone
        self.tipo_sanguineo = tps
        
    def __str__(self):
        return f'''
        {super().__str__()},
        Contato: {self.telefone},
        '''