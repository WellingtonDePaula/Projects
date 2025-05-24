class Pessoa:
    def __init__(self, nome, email, dt_nasc):
        self.nome = nome
        self.email = email
        self.data_nascimento = dt_nasc

    def __str__(self):
        return f'''
        Nome: {self.nome}, 
        Email: {self.email}, 
        Nascido(a) em: {self.data_nascimento}'''


class Paciente(Pessoa):
    def __init__(self, nome, email, dt_nasc, telefone, tps):
        super().__init__(nome, email, dt_nasc)
        self.telefone = telefone
        self.tipo_sanguineo = tps

    def __str__(self):
        return f'''
        {super().__str__()},
        Contato: {self.telefone},
        '''

class Medico(Pessoa):
    def __init__(self, nome, email, dt_nasc, crm, espec):
        super().__init__(nome, email, dt_nasc)
        self.CRM = crm
        self.especialidade = espec
    
    def __str__(self):
        return f'''
        {super().__str__()},
        CRM: {self.CRM},
        Especialidade: {self.especialidade},
        '''

def main():
    med = Medico("Gerivaldo", "gerivaldoDaSilva@gmail.com", "16/05/1980", 29481, "Odontologia")
    pac = Paciente("Marilda", "marildasfadina@gmail.com", "10/02/2003", "+55 47 99284-2456", "O+")

    print(med.__str__())
    print(pac.__str__())

main()