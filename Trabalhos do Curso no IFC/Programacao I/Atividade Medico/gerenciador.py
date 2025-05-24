from medico import Medico
from paciente import Paciente
from menu import Menu

class Gerenciador:
    def __init__(self):
        self.pacientes = []
        self.medicos = []
        self.logado = None
    
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
    
    def removerPaciente(self, cpf):
        for i in range(len(self.pacientes)):
            if(self.pacientes[i].cpf == cpf):
                self.pacientes[i].removido()
                self.pacientes.pop(i)
                return
        print(f"Paciente não encontrado para o cpf: {cpf}")

    def cadastrarMedico(self, nome, email, dt_nasc, cpf, crm, espec):
        medico = Medico(nome, email, dt_nasc, cpf, crm, espec)
        self.medicos.append(medico)
    
    def cadastrarPaciente(self, nome, email, dt_nasc, cpf, telefone, tps):
        paciente = Paciente(nome, email, dt_nasc, cpf, telefone, tps)
        self.pacientes.append(paciente)

if(__name__ == "__main__"):
    gerenciador = Gerenciador()


    m = Menu(gerenciador)

    m.rodarMenu()