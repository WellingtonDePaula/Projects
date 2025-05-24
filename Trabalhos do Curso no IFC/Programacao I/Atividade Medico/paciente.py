from pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome, email, dt_nasc, cpf, telefone, tps):
        super().__init__(nome, email, dt_nasc)
        self.telefone = telefone
        self.tipo_sanguineo = tps
        self.cpf = cpf
        self.consultas = []
    
    def listarConsultas(self):
        for consulta in self.consultas:
            print(consulta.__str__())

    def desmarcarConsulta(self, data, horario):
        for i in range(len(self.consultas)):
            if(self.consultas[i].data == data and self.consultas[i].horario == horario):
                self.consultas[i].desmarcarConsulta()
                return

    def __str__(self):
        return f'''
        {super().__str__()},
        Contato: {self.telefone},
        '''