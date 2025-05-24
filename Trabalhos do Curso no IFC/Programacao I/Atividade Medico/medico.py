from pessoa import Pessoa
from consulta import Consulta

class Medico(Pessoa):
    def __init__(self, nome, email, dt_nasc, cpf, crm, espec):
        super().__init__(nome, email, dt_nasc)
        self.CRM = crm
        self.especialidade = espec
        self.cpf = cpf
        self.consultas = []

    def listarPacientes(self):
        for consulta in self.consultas:
            paciente = consulta.paciente
            print(paciente.__str__())
    
    def listarConsultas(self):
        for i in range(len(self.consultas)):
            print(f"Consulta {i}")
            print(self.consultas[i].__str__())
    
    def marcarConsulta(self, data, horario, paciente):
        consulta = Consulta(data, horario, self, paciente)
        self.consultas.append(consulta)
        paciente.consultas.append(consulta)

    def desmarcarConsulta(self, data, horario):
        for i in range(len(self.consultas)):
            if(self.consultas[i].data == data and self.consultas[i].horario == horario):
                self.consultas[i].desmarcarConsulta()
                return
    
    def __str__(self):
        return f'''
        {super().__str__()},
        CRM: {self.CRM},
        Especialidade: {self.especialidade},
        '''