# -*- coding: utf-8 -*-

from Clase_DB import DB
class Dueno(object):
    id = None
    nombre = None
    apellido = None
    DNI = None
    telefono = None

    def SetDueno(self, nombre, apellido, DNI, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
        self.telefono = telefono

    def DeserializarDueno(self, diccionario_duenos):
        self.id = diccionario_duenos['id_dueno']
        self.nombre = diccionario_duenos['nombre']
        self.apellido = diccionario_duenos['apellido']
        self.DNI = diccionario_duenos['DNI']
        self.telefono = diccionario_duenos['telefono']

    def InsertarDueno(self, nombre, apellido, Dni, telefono):
        self.SetDueno(nombre, apellido, Dni, telefono)
        DB().run("INSERT INTO Duenos values(null,'" + self.nombre + "','" + self.apellido + "'," + str(self.DNI) + ",'" + self.telefono + "');")


    @staticmethod
    def SeleccionarDuenos():
        lista = []
        select_cursor = DB().run("Select * from Duenos;")
        for item in select_cursor:
            unDueno = Dueno()
            unDueno.DeserializarDueno(item)
            lista.append(unDueno)
        return lista

    @staticmethod
    def SeleccionarDuenosPorID(id):
        select_cursor = DB().run("Select * from Duenos where id_dueno = " + str(id) + ";")
        d = select_cursor.fetchall()
        unDueno = Dueno()
        unDueno.DeserializarDueno(d[0])
        return unDueno

    @staticmethod
    def BuscarDueno(id):
        lista_duenos = Dueno.SeleccionarDuenos()
        for item in lista_duenos:
            if item.id == id:
                return item

    def UpdateDueno(self, id):
        DB().run("Update Duenos set nombre = '" + self.nombre + "', apellido = '" + self.apellido + "', DNI = " + str(self.DNI) +", telefono = '" + self.telefono + "', id_dueno = " + str(self.id) + " where id_dueno = " + str(id) + ";")

    def DeleteDueno(self, id):
        DB().run("Delete from Duenos where id_dueno = " + str(id) +";")
