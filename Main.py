# -*- coding: utf-8 -*-
import os


#CAMBIAR BASE DE DATOS DE DUEÑOS A DUENOS

from Clase_Menu import Menu
from Clase_Dueno import Dueno
from Clase_Veterinario import Veterinario
from Clase_Macota import Mascota
from Clase_DB import DB
from Clase_Consulta import Consulta

DB().SetConection('127.0.0.1', 'root', 'alumno', 'TP2')


# charset = "utf8", autocommit = True)

loop = True
while(loop):
    os.system('cls')
    print("MENU")
    Menu.MenuPrincipal()
    opcion = input("Elija una opcion: ")
    if opcion == "1":
        while(loop):
            os.system('cls')
            print("DUENOS")
            Menu.MenuFunciones()
            opcion_duenos = input("Elija la funcion")

            if opcion_duenos == "1":
                        # INSERT DUENOS
                while (1):
                    os.system('cls')
                    print("PRINT DUENOS")
                    dueno = Dueno()
                    nombre = input("Ingrese nombre: ")

                    if nombre == 'Basta':
                      break

                    apellido = input("Ingrese apellido: ")
                    Dni = input("Ingrese DNI: ")
                    telefono = input("Ingrese telefono: ")
                    dueno.InsertarDueno(nombre, apellido, Dni, telefono)

            elif opcion_duenos == "2":
                os.system('cls')
                # UPDATE DUENOS
                print("UPDATE DUENOS")
                dueno_a_modificar = input("Ingrese el dueño a modificar: ")
                dueno = Dueno.SeleccionarDuenosPorID(dueno_a_modificar)
                nombre = input("Ingrese el nuevo nombre: ")
                apellido = input("Apellido: ")
                DNI = input("DNI: ")
                telefono = input("Telefono: ")
                dueno.SetDueno(nombre, apellido, DNI, telefono)
                dueno.UpdateDueno(dueno_a_modificar)
                dueno = Dueno.SeleccionarDuenosPorID(dueno_a_modificar)
                print("solito:" + dueno.nombre)

            elif opcion_duenos == "3":
                os.system('cls')
                print("DELETE DUENOS")
                dueno_a_borrar = input("Ingrese el dueño a borrar: ")
                dueno = Dueno.SeleccionarDuenosPorID(dueno_a_borrar)
                Dueno().DeleteDueno(dueno_a_borrar)

            elif opcion_duenos == "4":
                while(loop):
                    os.system('cls')
                    Menu.MenuSelects()
                    opcion_select_duenos = input("Elija la funcion: ")

                    if opcion_select_duenos == "1":
                        os.system('cls')
                        print("SELECT ALL DUENOS")
                        listaDuenos = Dueno.SeleccionarDuenos()
                        for item in listaDuenos:
                            print(item.id, item.nombre, item.apellido, item.DNI, item.telefono)

                    elif opcion_select_duenos == "2":
                        os.system('cls')
                        print("SELECT POR ID DUENOS")
                        dueno_a_seleccionar = input("Ingrese el dueno a seleccionar")
                        dueno = Dueno.SeleccionarDuenosPorID(dueno_a_seleccionar)
                        print(str(dueno.id), dueno.nombre, dueno.apellido, str(dueno.DNI), dueno.telefono)
                    elif opcion_select_duenos == "3":
                        break
                    elif opcion_select_duenos == "4":
                        loop = False
                    else: equivocacion_select_dueno = input("Opcion incorrecta")
            elif opcion_duenos == "5":
                break
            elif opcion_duenos == "6":
                loop = False
            else: equivocacion = input("Opcion incorrecta")

    elif opcion == "2":
        while (loop):
            os.system('cls')
            print("VETERINARIOS")
            Menu.MenuFunciones()
            opcion_veterinarios = input("Elija la funcion")

            if opcion_veterinarios == "1":
                # INSERT VETERINARIOS
                while(1):
                    os.system('cls')
                    print("INSERT VETERINARIOS")
                    Veterinariow = Veterinario()
                    nombre = input("Ingrese nombre: ")
                    if nombre == 'Basta':
                        break
                    apellido = input("Ingrese apellido: ")
                    Dni = input("Ingrese DNI: ")
                    sueldo = input("Ingrese sueldo: ")
                    Veterinariow.InsertarVeterinario(nombre, apellido, Dni, sueldo)


            elif opcion_veterinarios == "2":
                os.system('cls')
                # UPDATE VETERINARIOS
                print("UPDATE VETERINARIOS")
                veterinario_a_modificar = input("Ingrese el veterinario a modificar: ")
                veterinario = Veterinario.SeleccionarVeterinariosPorID(veterinario_a_modificar)
                nombre = input("Ingrese el nuevo nombre: ")
                apellido = input("Apellido: ")
                DNI = input("DNI: ")
                sueldo = input("Sueldo: ")
                veterinario.SetVeterinario(nombre, apellido, DNI, sueldo)
                veterinario.UpdateVeterinario(veterinario_a_modificar)

            elif opcion_veterinarios == "3":
                os.system('cls')
                print("DELETE VETERINARIOS")
                veterinario_a_borrar = input("Ingrese el veterinario a borrar: ")
                veterinario = Veterinario.SeleccionarVeterinariosPorID(veterinario_a_borrar)
                Veterinario.DeleteVeterinario(veterinario_a_borrar)

            elif opcion_veterinarios == "4":
                while(loop):
                    os.system('cls')
                    Menu.MenuSelects()
                    opcion_select_veterinarios = input("Elija la funcion: ")

                    if opcion_select_veterinarios == "1":
                        os.system('cls')
                        print("SELECT ALL VETERINARIOS")
                        listaveterinarios = Veterinario.SeleccionarVeterinarios()
                        for item in listaveterinarios:
                            print(item.id, item.nombre, item.apellido, item.DNI, item.sueldo)

                    elif opcion_select_veterinarios == "2":
                        os.system('cls')
                        print("SELECT POR ID VETERINARIOS")
                        veterinario_a_seleccionar = input("Ingrese el veterinario a seleccionar")
                        veterinario = Veterinario.SeleccionarVeterinariosPorID(veterinario_a_seleccionar)
                        print(str(veterinario.id), veterinario.nombre, veterinario.apellido, str(veterinario.DNI), veterinario.sueldo)
                    elif opcion_select_veterinarios == "3":
                        break
                    elif opcion_select_veterinarios == "4":
                        loop = False
                    else:   equivocacion_select_veterinario = input("Opcion incorrecta")
            elif opcion_veterinarios == "5":
                break
            elif opcion_veterinarios == "6":
                loop = False
            else:
                equivocacion = input("Opcion incorrecta")
    elif opcion == "3":
        while (loop):
            os.system('cls')
            print("INSERT MASCOTAS")
            Menu.MenuFunciones()
            opcion_mascotas = input("Elija la funcion")
            if opcion_mascotas == "1":
                while (1):
                    os.system('cls')
                    print("INSERT MASCOTAS")
                    mascota = Mascota()
                    nombre = input("Ingrese nombre: ")
                    if nombre == 'Basta':
                        break
                    tipo = input("Ingrese tipo: ")
                    dueno = input("Ingrese dueno: ")
                    mascota.InsertarMascota(nombre, tipo, dueno)
            elif opcion_mascotas == "2":
                os.system('cls')
                print("UPDATE MASCOTAS")
                mascota_a_modificar = input("Ingrese la mascota a modificar: ")
                mascota = Mascota.SelectMascotaporID(mascota_a_modificar)
                nombre = input("Ingrese el nuevo nombre: ")
                tipo = input("Tipo: ")
                dueno_id = input("ID de su dueno: ")
                mascota.SetMascota(nombre, tipo, dueno_id)
                mascota.UpdateMascota(mascota_a_modificar)
            elif opcion_mascotas == "3":
                os.system('cls')
                print("DELETE MASCOTAS")
                mascota_a_borrar = input("Ingrese la mascota a borrar: ")
                Mascota.DeleteMascota(mascota_a_borrar)
            elif opcion_mascotas == "4":
                while(loop):
                    os.system('cls')
                    Menu.MenuSelects()
                    opcion_select_mascotas = input("Elija la funcion: ")

                    if opcion_select_mascotas == "1":
                        os.system('cls')
                        print("SELECT ALL MASCOTAS")
                        listamascotas = Mascota.SelectMascota()
                        for item in listamascotas:
                            print(item.id, item.nombre, item.tipo, item.dueno.id)

                    elif opcion_select_mascotas == "2":
                        os.system('cls')
                        print("SELECT POR ID MASCOTAS")
                        mascota_a_seleccionar = input("Ingrese mascotas a seleccionar")
                        mascota = Mascota.SelectMascotaporID(mascota_a_seleccionar)
                        print(str(mascota.id), mascota.nombre, mascota.tipo, mascota.dueno.id)

                    elif opcion_select_mascotas == "3":
                        break
                    elif opcion_select_mascotas == "4":
                        loop = False
                    else:   equivocacion_select_mascotas = input("Opcion incorrecta")
            elif opcion_mascotas == "5":
                break
            elif opcion_mascotas == "6":
                loop = False
            else:
                equivocacion = input("Opcion incorrecta")
    elif opcion == "4":
        while (loop):
            os.system('cls')
            print("CONSULTAS")
            Menu.MenuFunciones()
            opcion_consultas = input("Elija la funcion")

            if opcion_consultas == "1":
                while (loop):
                    os.system('cls')
                    print("INSERT CONSULTAS")
                    consulta = Consulta()
                    continuar = input('Desea continuar?: ')
                    if continuar == "Basta":
                        break
                    precio = int(input("Inserte precio: "))
                    masscota = input("Inserte mascota: ")
                    diagnos = input("Inserte diagnostico: ")
                    vet = input("Inserte veterinario: ")
                    consulta.InsertarConsulta(precio, diagnos, masscota, vet)
            elif opcion_consultas == "2":
                os.system('cls')
                print("UPDATE CONSULTAS")
                consulta_a_modificar = input("Ingrese la consulta a modificar: ")
                consulta = Consulta.SelectConsultasPorID(consulta_a_modificar)
                precio = input("Ingrese el precio nuevo: ")
                diagnostico = input("Diagnostico: ")
                mascota = input("ID de la mascota: ")
                veterinario = input("ID del veterinario: ")
                consulta.SetConsulta(precio, diagnostico, mascota, veterinario)
                consulta.UpdateConsulta(consulta_a_modificar)
            elif opcion_consultas == "3":
                os.system('cls')
                print("DELETE CONSULTAS")
                consulta_a_borrar = input("Ingrese la consulta a borrar: ")
                Consulta.DeleteConsulta(consulta_a_borrar)
            elif opcion_consultas == "4":
                while(loop):
                    os.system('cls')
                    Menu.MenuSelects()
                    opcion_select_consultas = input("Elija la funcion: ")

                    if opcion_select_consultas == "1":
                        os.system('cls')
                        print("SELECT ALL CONSULTAS")
                        listaconsultas = Consulta.SelectConsultas()
                        for item in listaconsultas:
                            print(item.id, item.precio, item.diagnostico, item.mascota.id, item.veterinario.id)

                    elif opcion_select_consultas == "2":
                        os.system('cls')
                        print("SELECT POR ID CONSULTAS")
                        consulta_a_seleccionar = input("Ingrese la consulta a seleccionar")
                        consulta = Consulta.SelectConsultasPorID(consulta_a_seleccionar)
                        print(str(consulta.id), consulta.precio, consulta.diagnostico, consulta.mascota.id, consulta.veterinario.id)
                    elif opcion_select_consultas == "3":
                        break
                    elif opcion_select_consultas == "4":
                        loop = False
                    else: equivocacion_select_consulta = input("Opcion incorrecta")
            elif opcion_consultas == "5":
                break
            elif opcion_consultas == "6":
                loop = False
    elif opcion == "5":
        loop = False
    else:
        otre = input("Opcion incorrecta")
