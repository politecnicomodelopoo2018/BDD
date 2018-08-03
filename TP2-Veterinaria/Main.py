# -*- coding: utf-8 -*-
import pymysql


#CAMBIAR BASE DE DATOS DE DUEÑOS A DUENOS

from Clase_Dueno import Dueno
from Clase_Veterinario import Veterinario
from Clase_Macota import Mascota
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
'''

# SELECT DUENOS
'''
listaDuenos = Dueno.SeleccionarDuenos()
dueno = Dueno.SeleccionarDuenosPorID(9)

for item in listaDuenos:
    print(item.nombre)

print("solito:" + dueno.nombre)
'''
#UPDATE DUENOS
'''
dueno.nombre = "Ayelen"
dueno.UpdateDueno(9)

dueno = Dueno.SeleccionarDuenosPorID(9)
print("solito:" + dueno.nombre)
'''

# DELETE DUENOS
'''
coso.DeleteDueno(10)
'''

#VETERINARIOS

#INSERT VETERINARIOS!!!1!!

'''
while(1):
    Veterinariow = Veterinario()
    nombre = input("Ingrese nombre: ")
    if nombre == 'Basta':
        break
    apellido = input("Ingrese apellido: ")
    Dni = input("Ingrese DNI: ")
    sueldo = input("Ingrese sueldo: ")
    Veterinariow.InsertarVeterinario(nombre, apellido, Dni, sueldo)
'''
#SELECT VETERINARIO
'''
veterinario = Veterinario()
listaveterinarios = veterinario.SeleccionarVeterinarios()
veterinariosolo = veterinario.SeleccionarVeterinariosPorID(1)

for item in listaveterinarios:
    print(item.nombre)
    print(item.sueldo)


veterinariosolo.nombre = "Aye"
veterinariosolo.UpdateVeterinario(1)
print(veterinariosolo.nombre)
'''
'''
#DELETE VETERINARIOS
VETERINARIO = Veterinario()
VETERINARIO.DeleteVeterinario(2)
'''

listamascota = Mascota.SelectMascota()
mascotasola = Mascota.SelectMascotaporID(2)

for item in listamascota:
    print(item.nombre)
    print(item.tipo)

print("Mascota sola: " + mascotasola.nombre)