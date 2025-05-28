from medico import Medico
from paciente import Paciente
from consulta import Consulta
from menu import Menu

class Gerenciador:
    def __init__(self):
        self.pacientes = []
        self.medicos = []
        self.consultas = []
        self.logado = None
    
    def cadastrarPaciente(self, nome, email, dt_nasc, cpf, telefone, tps):
        paciente = Paciente(nome, email, dt_nasc, cpf, telefone, tps)
        self.pacientes.append(paciente)
    
    def cadastrarMedico(self, nome, email, dt_nasc, cpf, crm, espec):
        medico = Medico(nome, email, dt_nasc, cpf, crm, espec)
        self.medicos.append(medico)
    
    def procuraMedico(self, cpf):
        for medico in self.medicos:
            if(medico.cpf == cpf):
                return medico
        print(f"Médico não encontrado para o cpf: {cpf}")
        return None
    
    def procuraPaciente(self, cpf):
        for paciente in self.pacientes:
            if(paciente.cpf == cpf):
                return paciente
        print(f"Paciente não encontrado para o cpf: {cpf}")
        return None
    
    def logar(self, tipo, cpf, senha):
        if(tipo == "M"):
            medico = self.procuraMedico(cpf)
            if(medico.senha == senha):
                self.logado = medico
        if(tipo == "P"):
            paciente = self.procuraPaciente(cpf)
            if(paciente.senha == senha):
                self.logado = paciente
        print("Senha e/ou cpf inválidos")
        self.logado = None
    
    def listarConsultas(self):
        for i in range(len(self.logado.consultas)):
            print(i)
            print(self.logado.consultas[i].__str__())
    
    def marcarConsulta(self, data, horario, cpfPaciente):
        paciente = self.procuraPaciente(cpfPaciente)
        if(paciente):
            consulta = Consulta(data, horario, self.logado, paciente)
            self.consultas.append(consulta)
    
    def desmarcarConsulta(self, data, horario):
        for i in range(len(self.consultas)):
            if(self.consultas[i].data == data and self.consultas[i].horario == horario):
                self.consultas.pop(i)
    
    def removerPaciente(self, cpf):
        paciente = self.procuraPaciente(cpf)
        
        for i in range(len(self.consultas)):
            if(self.consultas[i].paciente == paciente):
                self.consultas.pop(i)
        self.pacientes.remove(cpf)
    
if(__name__ == "__main__"):
    gerenciador = Gerenciador()

    m = Menu(gerenciador)

    m.rodarMenu()