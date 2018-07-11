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

    def InsertarDueno(self, nombre, apellido, Dni, telefono):
        self.SetDueno(nombre, apellido, Dni, telefono)
        DB().run("INSERT INTO Duenos values(null,'" + self.nombre + "','" + self.apellido + "'," + str(self.DNI) + ",'" + self.telefono + "');")

    def SeleccionarDuenos()