import csv


class CHCapi:
    def __init__(self, path):
        self.path = path
        self.pacientes = self.getPacientes()

    def getPacientes(self):
        data = []
        with open(self.path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                data.append(row)
        return data

    def buscarPaciente(self, idPaciente):
        id = str(idPaciente)
        pacienteAlvo = []
        for paciente in self.pacientes:
            if(paciente[0] == id):
                pacienteAlvo = paciente
                break
        return pacienteAlvo


api = CHCapi('src/app/api/pacientes.csv')
