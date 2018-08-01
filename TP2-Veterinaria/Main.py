# -*- coding: utf-8 -*-
import pymysql


#CAMBIAR BASE DE DATOS DE DUEÑOS A DUENOS

from Clase_Dueno import Dueno
from Clase_DB import DB
DB().SetConection('127.0.0.1', 'root', 'alumno', 'TP2')


# charset = "utf8", autocommit = True)
# INSERT DUENOS
'''
while(1):
    dueno = Dueno()
    nombre = input("Ingrese nombre: ")
    if nombre == 'Basta':
        break
    apellido = input("Ingrese apellido: ")
    Dni = input("Ingrese DNI: ")
    telefono = input("Ingrese telefono: ")
    dueno.InsertarDueno(nombre, apellido, Dni, telefono)

#UPDATE DUENOS
coso = Dueno()
coso.UpdateDueno("nombre", "Camila", 9)
coso.UpdateDueno("apellido", "Reynoso", 9)

# DELETE DUENOS
coso.DeleteDueno(10)
'''
# SELECT DUENOS

listaDuenos = Dueno.SeleccionarDuenos()
dueno = Dueno.SeleccionarDuenosPorID(9)

for item in listaDuenos:
    print(item.nombre)
print("solito:" + dueno.nombre)

'''
Persona_dueno = Dueno()
print(Persona_dueno)
Persona_dueno.SeleccionarDuenos(9)

'''
