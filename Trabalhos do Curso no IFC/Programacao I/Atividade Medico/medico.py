from pessoa import Pessoa
from consulta import Consulta

class Medico(Pessoa):
    def __init__(self, nome, email, dt_nasc, cpf, senha, crm, espec):
        super().__init__(nome, email, dt_nasc, cpf, senha)
        self.CRM = crm
        self.especialidade = espec
    
    def __str__(self):
        return f'''
        {super().__str__()},
        CRM: {self.CRM},
        Especialidade: {self.especialidade},
        '''