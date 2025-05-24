class Menu:
    def __init__(self, gerenciador):
        self.opcoes = []
        self.gerenciador = gerenciador
        print("Seja bem vindo ao meu sistema de clinica!")
    
    def loginOuCadastro(self):
        while(not self.gerenciador.logado):
            print()
            print("1- Logar")
            print("2- Cadastrar")
            escolha = int(input("--> "))

            if(escolha == 1):
                cpf = input("Digite seu cpf: ")
                self.gerenciador.logado = self.logar(cpf)
            
            if(escolha == 2):
                if(self.tipo == "M"):
                    self.cadastrarMedico()
                if(self.tipo == "P"):
                    self.cadastrarPaciente()
            
    
    def logar(self, login):
        if(self.tipo == "M"):
            result = self.gerenciador.procuraMedico(login)
        if(self.tipo == "P"):
            result = self.gerenciador.procuraPaciente(login)
        return result

    def cadastrarMedico(self):
        #self, nome, email, dt_nasc, cpf, crm, espec
        nome = input("Nome -> ")
        email = input("Email -> ")
        dt_nasc = input("Data de Nascimento -> ")
        cpf = input("Cpf -> ")
        crm = input("CRM -> ")
        espec = input("Especialização -> ")
        self.gerenciador.cadastrarMedico(nome, email, dt_nasc, cpf, crm, espec)

    def cadastrarPaciente(self):
        #self, nome, email, dt_nasc, cpf, telefone, tps
        nome = input("Nome -> ")
        email = input("Email -> ")
        dt_nasc = input("Data de Nascimento -> ")
        cpf = input("Cpf -> ")
        telefone = input("Telefone -> ")
        tps = input("Tipo Sanguíneo -> ")
        self.gerenciador.cadastrarPaciente(nome, email, dt_nasc, cpf, telefone, tps)

    def removerPaciente(self):
        cpf = input("Cpf do paciente a ser removido --> ")
        self.gerenciador.removerPaciente(cpf)
    
    def marcarConsulta(self):
        data = input("Data da consulta --> ")
        horario = input("Horário da consulta --> ")
        
        pacienteCpf = input("Cpf do paciente da consulta --> ")
        paciente = self.gerenciador.procuraPaciente(pacienteCpf)

        # print(paciente)

        self.gerenciador.logado.marcarConsulta(data, horario, paciente)

    def desmarcarConsulta(self):
        data = input("Data da consulta --> ")
        horario = input("Horário da consulta --> ")
        self.gerenciador.logado.desmarcarConsulta(data, horario)

    def desenhaMenu(self):
        for opcao in self.opcoes:
            print(opcao)

    def rodarMenu(self):
        while(True):
            self.tipo = input("Você é um médico(M) ou paciente(P)?\n--> ")
            self.loginOuCadastro()
            
            while(self.gerenciador.logado):
                if(self.tipo == "M"):
                    self.opcoes = ["1- Cadastrar Paciente", "2- Remover Paciente", "3- Listar Pacientes", "4- Marcar Consulta", "5- Listar Consultas", "6- Desmarcar Consulta", "7- Voltar"]
                    self.desenhaMenu()
                    escolha = int(input("--> "))
                    match escolha:
                        case 1:
                            self.cadastrarPaciente()
                        case 2:
                            self.removerPaciente()
                        case 3:
                            self.gerenciador.logado.listarPacientes()
                        case 4:
                            self.marcarConsulta()
                        case 5:
                            self.gerenciador.logado.listarConsultas()
                        case 6:
                            self.desmarcarConsulta()
                        case 7:
                            self.gerenciador.logado = None
                        
                if(self.tipo == "P"):
                    self.opcoes = ["1- Desmarcar consulta", "2- Listar consultas", "3- Voltar"]
                    self.desenhaMenu()
                    escolha = int(input("--> "))
                    match escolha:
                        case 1:
                            self.desmarcarConsulta()
                        case 2:
                            self.gerenciador.logado.listarConsultas()
                        case 3:
                            self.gerenciador.logado = None
        #self.desenhaMenu()
        # opcao = input("\nQual opção você deseja?\n--> ")