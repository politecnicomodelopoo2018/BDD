from Clase_Macota import Mascota
from Clase_Veterinario import Veterinario
from Clase_DB import DB

class Consulta(object):
    id_consulta = None
    precio = None
    diagnostico = None
    id_mascota = None
    id_veterinario = None

    def SetConsulta(self, precio, diagnostico, id_mascota, id_veterinario):
        self.precio = precio
        self.diagnostico = diagnostico
        self.id_mascota = id_mascota
        self.id_veterinario = id_veterinario


    def DeserializarConsultas(self, consulta_dicc):
        mascot = Mascota()
        veter = Veterinario()
        self.id_consulta = consulta_dicc["id_consulta"]
        self.precio = consulta_dicc["precio"]
        self.diagnostico = consulta_dicc["diagnostico"]
        idMascota = consulta_dicc["Mascotas_id_mascota"]
        mascot = Mascota.BuscarMascota(idMascota)
        self.id_mascota = mascot.BuscarMascota(idMascota)
        idVeterinario = consulta_dicc["Veterinarios_id_veterinario"]
        veter = Veterinario.BuscarVeterinario(idVeterinario)
        self.id_veterinario = veter.BuscarVeterinario(idVeterinario)


    @staticmethod
    def SelectConsultas():
        lista = []
        cursorpiola = DB().run = ("Select * from Consulta;")
        for itemm in cursorpiola:
            consul = Consulta()
            consul.DeserializarConsultas(itemm)
            lista.append(consul)
        return lista

    @staticmethod
    def SelectConsultasPorID(id):
        cursorxd = DB().run("select * from Consulta where id_consulta =" + str(id) + ";")
        consultaw = Consulta()
        consultaw.DeserializarConsultas.fetchall(cursorxd[0])
        return consultaw


    def InsertarConsulta(self, precio, diagnostico, mascota, vet):
        self.SetConsulta(precio, diagnostico, mascota, vet)
        DB().run("insert into Consulta values(NULL," + str(self.precio) + "," + self.diagnostico + "," + str(self.id_mascota) + "," + str(self.id_veterinario) + ");")
