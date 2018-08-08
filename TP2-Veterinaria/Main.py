# -*- coding: utf-8 -*-
import pymysql


#CAMBIAR BASE DE DATOS DE DUEÑOS A DUENOS

from Clase_Dueno import Dueno
from Clase_Veterinario import Veterinario
from Clase_Macota import Mascota
from Clase_DB import DB
from Clase_Consulta import Consulta

DB().SetConection('127.0.0.1', 'root', 'alumno', 'TP2')


# charset = "utf8", autocommit = True)
# INSERT DUENOS
'''
while(1):
    print("DUENOS")
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
    print("VETERINARIOS")
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
'''
#UPDATE VET
'''
veterinariosolo.nombre = "Aye"
veterinariosolo.UpdateVeterinario(1)
print(veterinariosolo.nombre)
'''

#DELETE VETERINARIOS
'''
VETERINARIO = Veterinario()
VETERINARIO.DeleteVeterinario(2)
'''


# MASCOTAS
'''
listamascota = Mascota.SelectMascota()
mascotasola = Mascota.SelectMascotaporID(2)

for item in listamascota:
    print(item.nombre)
    print(item.tipo)

print("Mascota sola: " + mascotasola.nombre)
'''
#MASCOTAS

#INSERT MASCOTAS
mascota = Mascota()
'''
while(1):
    print("Mascotas")
    mascota = Mascota()
    nombre = input("Ingrese nombre: ")
    if nombre == 'Basta':
        break
    tipo = input("Ingrese tipo: ")
    dueno = input("Ingrese dueno: ")
    mascota.InsertarMascota(nombre, tipo, dueno)
'''
#UPDATE MASCOTAS
'''
mascota.nombre = "mantecol"
mascota.UpdateMascota(2)
'''

# DELETE MASCOTAS
'''
mascota.DeleteMascota(2)
'''

# CONSULTAS


while(1):
    print("CONSULTAS")
    consulta = Consulta()
    precio = input("Inserte precio: ")
    if precio == "Basta":
        break
    masscota = input("Inserte mascota: ")
    diagnos = input("Inserte diagnostico: ")
    vet = input("Inserte veterinario: ")
    consulta.InsertarConsulta(precio, diagnos, masscota, vet)




LISTAAA = consulta.SelectConsultas()
CON = consulta.SelectConsultasPorID(1)

for item in LISTAAA:
    print (item.id_consulta)

print("solo: " + CON.id_consulta)

