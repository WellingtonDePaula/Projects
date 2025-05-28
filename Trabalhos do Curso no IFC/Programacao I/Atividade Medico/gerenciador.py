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

        self.cadastrarPaciente("Carlos Mendes", "carlos.mendes@example.com", "15/04/1990", "123.123.123-00", "rumoAVitória", "(11) 91234-5678", "A+")
        self.cadastrarPaciente("Aline Souza", "aline.souza@example.com", "17/10/1995", "678.678.678-55", "joiasDeFamilia", "(61) 96789-0123", "O-")

        self.cadastrarMedico("Cláudio", "claudio123@example.com", "15/04/1978", "958.437.540-73", "amoMeusGatos1", "CRM-SP 123456", "Urologia")
        self.cadastrarMedico("Renata", "renata@example.com", "12/09/1975", "678.901.234-55", "naoMeFaçaFalar!", "CRM-SP 334455", "Neurologia")
    
    def cadastrarPaciente(self, nome, email, dt_nasc, cpf, senha, telefone, tps):
        paciente = Paciente(nome, email, dt_nasc, cpf, senha, telefone, tps)
        self.pacientes.append(paciente)
    
    def cadastrarMedico(self, nome, email, dt_nasc, cpf, senha, crm, espec):
        medico = Medico(nome, email, dt_nasc, cpf, senha, crm, espec)
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
                return
        if(tipo == "P"):
            paciente = self.procuraPaciente(cpf)
            if(paciente.senha == senha):
                self.logado = paciente
                return
        print("Senha e/ou cpf inválidos")
        self.logado = None
    
    def listarConsultas(self):
        for consulta in self.consultas:
            if(consulta.medico == self.logado or consulta.paciente == self.logado):
                print(consulta.__str__())
        
        print(f"\nNão há consultas cadastradas para o usuário: {self.logado.nome}")
    
    def marcarConsulta(self, data, horario, cpfPaciente):
        paciente = self.procuraPaciente(cpfPaciente)
        if(paciente):
            consulta = Consulta(data, horario, self.logado, paciente)
            self.consultas.append(consulta)
    
    def desmarcarConsulta(self, data, horario):
        for i in range(len(self.consultas)):
            if(self.consultas[i].data == data and self.consultas[i].horario == horario and self.consultas[i].medico == self.logado or self.consultas[i].data == data and self.consultas[i].horario == horario and self.consultas[i].paciente == self.logado):
                self.consultas.pop(i)
                return
        print(f"\nNenhuma consulta encontrada para o usuário: {self.logado.nome}, na data: {data}, as: {horario} horas")
    
    def removerPaciente(self, cpf):
        paciente = self.procuraPaciente(cpf)
        
        for i in range(len(self.consultas)):
            if(self.consultas[i].paciente == paciente):
                self.consultas.pop(i)
        
        self.pacientes.remove(cpf)
    
    def listarPacientes(self):
        for consulta in self.consultas:
            if(consulta.medico == self.logado):
                print(consulta.paciente.__str__())
        
        print(f"\nNão há pacientes cadastrados para o usuário: {self.logado.nome}")

if(__name__ == "__main__"):
    gerenciador = Gerenciador()

    m = Menu(gerenciador)

    m.rodarMenu()