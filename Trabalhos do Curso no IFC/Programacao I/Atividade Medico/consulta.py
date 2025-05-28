class Consulta:
    def __init__(self, data: str, horario: str, medico, paciente):
        self.data = data
        self.horario = horario
        
        self.medico = medico
        self.paciente = paciente
        
    def __str__(self):
        return f'''
        Data: {self.data}, 
        Horário: {self.horario}, 
        Médico: {self.medico}
        Paciente: {self.paciente}'''