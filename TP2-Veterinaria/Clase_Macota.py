from Clase_DB import DB
from Clase_Dueno import Dueno

class Mascota(object):
    id = None
    nombre = None
    tipo = None
    dueno = None

    def SetMascota(self, nombre, tipo, dueno):
        self.nombre = nombre
        self.tipo = tipo
        self.dueno = dueno

    def DeserializarMascota(self, dicc_mascotas):
        dueno_obj = Dueno()
        self.id = dicc_mascotas['id_mascota']
        self.nombre = dicc_mascotas['nombre']
        self.tipo = dicc_mascotas['tipo']
        id_del_dueno = dicc_mascotas['Duenos_id_duenos']
        dueno_obj = Dueno.BuscarDueno(id_del_dueno)  # foreign ki
        self.dueno = dueno_obj

    @staticmethod
    def SelectMascota():
        listam = []
        select_cursor = DB().run("Select * from Mascotas;")
        for item in select_cursor:
            mascota = Mascota()
            mascota.DeserializarMascota(item)
            listam.append(mascota)
        return listam

    @staticmethod
    def SelectMascotaporID(id):
        select_cursor = DB().run("Select * from Mascotas where id_mascota = " + str(id) + ";")
        d = select_cursor.fetchall()
        mascota = Mascota()
        mascota.DeserializarMascota(d[0])
        return mascota

    @staticmethod
    def BuscarMascota(id):
        mc = Mascota()
        listaa = mc.SeleccionarVeterinarios()
        for item in listaa:
            if item == id:
                return item


    def InsertarMascota(self, nombre, tipo, dueno):
        self.SetMascota(nombre, tipo, dueno)
        DB().run("insert into Mascotas values(NULL,'" + self.nombre + "','" + self.tipo + "'," + self.dueno + ");")

    def UpdateMascota(self, id):
        DB().run("Update Mascotas set nombre = '" + self.nombre + "', tipo = '" + self.tipo + "', dueno = " + self.dueno + "where id_mascota = " + str(id) + ";")

    def DeleteMascota(self, id):
        DB().run("Delete from Mascotas where id_mascota = " + str(id) + ";")

