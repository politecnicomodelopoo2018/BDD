# -*- coding: utf-8 -*-
import pymysql


#CAMBIAR BASE DE DATOS DE DUEÑOS A DUENOS

from Clase_Dueno import Dueno
from Clase_DB import DB
DB().SetConection('127.0.0.1', 'root', 'alumno', 'TP2')


# charset = "utf8", autocommit = True)
while(1):
    dueno = Dueno()
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    Dni = input("Ingrese DNI: ")
    telefono = input("Ingrese telefono: ")
    dueno.InsertarDueno(nombre, apellido, Dni, telefono)

select_cursor = DB().run("Select * from Duenos;")

for item in select_cursor:
    print (item['nombre'])



