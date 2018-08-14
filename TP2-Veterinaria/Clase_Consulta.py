from Clase_Macota import Mascota
from Clase_Veterinario import Veterinario
from Clase_DB import DB

class Consulta(object):
    id = None
    precio = None
    diagnostico = None
    mascota = None
    veterinario = None

    def SetConsulta(self, precio, diagnostico, id_mascota, id_veterinario):
        self.precio = precio
        self.diagnostico = diagnostico
        mascota = Mascota.SelectMascotaporID(id_mascota)
        self.mascota = mascota
        veterinario = Veterinario.SeleccionarVeterinariosPorID(id_veterinario)
        self.veterinario = veterinario

    def DeserializarConsultas(self, consulta_dicc):
        self.id = consulta_dicc['id_consulta']
        self.precio = consulta_dicc['precio']
        self.diagnostico = consulta_dicc['diagnostico']
        idMascota = consulta_dicc['Mascotas_id_mascota']
        self.mascota = Mascota.BuscarMascota(idMascota)
        idVeterinario = consulta_dicc['Veterinarios_id_veterinario']
        self.veterinario = Veterinario.BuscarVeterinario(idVeterinario)

    @staticmethod
    def SelectConsultas():
        lista = []
        cursorpiola = DB().run ("Select * from Consulta;")
        for itemm in cursorpiola:
            consul = Consulta()
            consul.DeserializarConsultas(itemm)
            lista.append(consul)
        return lista

    @staticmethod
    def SelectConsultasPorID(idd):
        cursorxd = DB().run("select * from Consulta where id_consulta =" + str(idd) + ";")
        d = cursorxd.fetchall()
        consulta = Consulta()
        consulta.DeserializarConsultas(d[0])
        return consulta


    def InsertarConsulta(self, precio, diagnostico, mascota, vet):
        self.SetConsulta(precio, diagnostico, mascota, vet)
        DB().run("insert into Consulta values(NULL," + str(self.precio) + ",'" + self.diagnostico + "'," + str(self.veterinario.id) + "," + str(self.mascota.id) + ");")

    def UpdateConsulta(self, idd):
        DB().run("Update Consulta set id_consulta = " + str(self.id) + ", precio = " + str(self.precio) + ", diagnostico = '" + self.diagnostico + "', Veterinarios_id_veterinario = " + str(self.veterinario.id) + ", Mascotas_id_mascota = " + str(self.mascota.id) + " where id_consulta = " + str(idd) + ";")

    @staticmethod
    def DeleteConsulta(id):
        DB().run("Delete from Consulta where id_consulta = " + str(id) + ";")

