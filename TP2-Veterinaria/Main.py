# -*- coding: utf-8 -*-
import pymysql


#CAMBIAR BASE DE DATOS DE DUEÑOS A DUENOS

from Clase_Menu import Menu
from Clase_Dueno import Dueno
from Clase_Veterinario import Veterinario
from Clase_Macota import Mascota
from Clase_DB import DB
from Clase_Consulta import Consulta

DB().SetConection('127.0.0.1', 'root', 'alumno', 'TP2')


# charset = "utf8", autocommit = True)


while(1):
    print("MENU")
    Menu.MenuPrincipal()
    opcion = input("Elija una opcion: ")
    if opcion == "1":
        print("DUENOS")
        Menu.MenuFunciones()
        opcion1 = input("Duenos")
    elif opcion == "2":
        print("VETERINARIOS")
        Menu.MenuFunciones()
        opcion1 = input("veterinarios")
    elif opcion == "3":
        print("MASCOTAS")
        Menu.MenuFunciones()
        opcion1 = input("mascotas")
    elif opcion == "4":
        print("CONSULTAS")
        Menu.MenuFunciones()
        opcion1 = input("consultas")
    else:
        print("Opcion incorrecta, ingrese otre")
        otre = input("hole")


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
mascota = Mascota.SelectMascotaporID(6)
print(mascota.nombre, mascota.dueno.id)
mascota.nombre = "mantecol"
mascota.UpdateMascota(6)

'''
# DELETE MASCOTAS
'''
mascota.DeleteMascota(2)
'''

# INSERT CONSULTAS
'''

while(1):
    print("CONSULTAS")
    consulta = Consulta()
    continuar = input('Desea continuar?: ')
    if continuar == "Basta":
        break
    precio = int(input("Inserte precio: "))
    masscota = input("Inserte mascota: ")
    diagnos = input("Inserte diagnostico: ")
    vet = input("Inserte veterinario: ")
    consulta.InsertarConsulta(precio, diagnos, masscota, vet)

CON = None
'''

# UPDATE CONSULTAS
'''

CON.id_mascota = Mascota.SelectMascotaporID(12)
CON.UpdateConsulta(4)
'''

# DELETE CONSULTAS
'''

CON = Consulta.SelectConsultasPorID(4)
Consulta.DeleteConsulta(4)
'''

# SELECT CONSULTAS
'''

LISTAAA = Consulta.SelectConsultas()

for item in LISTAAA:
    print (item.id, item.diagnostico)

CON = Consulta.SelectConsultasPorID(4)
print("solo: " + str(CON.id), CON.diagnostico, CON.id_mascota.id, CON.id_veterinario.id )
'''
