# -*- coding: utf-8 -*-



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
    print("MENU")
    Menu.MenuPrincipal()
    opcion = input("Elija una opcion: ")
    if opcion == "1":
        while(loop):
            print("DUENOS")
            Menu.MenuFunciones()
            opcion_duenos = input("Elija la funcion")

            if opcion_duenos == "1":
                        # INSERT DUENOS
                while (1):
                    print("INSERT DUENOS")
                    dueno = Dueno()
                    nombre = input("Ingrese nombre: ")

                    if nombre == 'Basta':
                      break

                    apellido = input("Ingrese apellido: ")
                    Dni = input("Ingrese DNI: ")
                    telefono = input("Ingrese telefono: ")
                    dueno.InsertarDueno(nombre, apellido, Dni, telefono)

            elif opcion_duenos == "2":
                # UPDATE DUENOS
                print("UPDATE DUENOS")
                dueno_a_modificar = input("Ingrese el dueño a modificar: ")
                error = False
                try:
                    dueno = Dueno.SeleccionarDuenosPorID(dueno_a_modificar)
                except IndexError:
                    print("Usuario no existente")
                    error = True
                if error == False:
                    nombre = input("Ingrese el nuevo nombre: ")
                    apellido = input("Apellido: ")
                    DNI = input("DNI: ")
                    telefono = input("Telefono: ")
                    dueno.SetDueno(nombre, apellido, DNI, telefono)
                    dueno.UpdateDueno(dueno_a_modificar)

            elif opcion_duenos == "3":
                print("DELETE DUENOS")
                dueno_a_borrar = input("Ingrese el dueño a borrar: ")
                error = False
                try:
                    dueno = Dueno.SeleccionarDuenosPorID(dueno_a_borrar)
                except IndexError:
                    print("Usuario no existente")
                    error = True
                if error == False:
                    try:
                        Dueno().DeleteDueno(dueno_a_borrar)
                    except:
                        print("Este dueno es una clave foranea y por tanto no se puede eliminar")
            elif opcion_duenos == "4":
                while(loop):
                    Menu.MenuSelects()
                    opcion_select_duenos = input("Elija la funcion: ")
                    error = False
                    if opcion_select_duenos == "1":
                        print("SELECT ALL DUENOS")
                        try:
                            listaDuenos = Dueno.SeleccionarDuenos()
                        except IndexError:
                            print("No hay ningun dueno, ingrese uno")
                            error = True
                        if error == False:
                            for item in listaDuenos:
                                print(item.id, item.nombre, item.apellido, item.DNI, item.telefono)

                    elif opcion_select_duenos == "2":
                        print("SELECT POR ID DUENOS")
                        dueno_a_seleccionar = input("Ingrese el dueno a seleccionar")
                        error = False
                        try:
                            dueno = Dueno.SeleccionarDuenosPorID(dueno_a_seleccionar)
                        except IndexError:
                            print("Usuario no existente")
                            error = True
                        if error == False:
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
            print("VETERINARIOS")
            Menu.MenuFunciones()
            opcion_veterinarios = input("Elija la funcion")

            if opcion_veterinarios == "1":
                # INSERT VETERINARIOS
                while(1):
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
                # UPDATE VETERINARIOS
                print("UPDATE VETERINARIOS")
                error = False
                veterinario_a_modificar = input("Ingrese el veterinario a modificar: ")
                try:
                    veterinario = Veterinario.SeleccionarVeterinariosPorID(veterinario_a_modificar)
                except IndexError:
                    error = True
                    print("Usuario no existente")
                if error == False:
                    nombre = input("Ingrese el nuevo nombre: ")
                    apellido = input("Apellido: ")
                    DNI = input("DNI: ")
                    sueldo = input("Sueldo: ")
                    veterinario.SetVeterinario(nombre, apellido, DNI, sueldo)
                    veterinario.UpdateVeterinario(veterinario_a_modificar)

            elif opcion_veterinarios == "3":
                print("DELETE VETERINARIOS")
                veterinario_a_borrar = input("Ingrese el veterinario a borrar: ")
                error = False
                try:
                    veterinario = Veterinario.SeleccionarVeterinariosPorID(veterinario_a_borrar)
                except IndexError:
                    print("Usuario no existente")
                    error = True
                if error == False:
                    try:
                        Veterinario.DeleteVeterinario(veterinario_a_borrar)
                    except:
                        print("Este veterinario es una clave foranea y por tanto no se puede eliminar")
            elif opcion_veterinarios == "4":
                while(loop):
                    Menu.MenuSelects()
                    opcion_select_veterinarios = input("Elija la funcion: ")
                    if opcion_select_veterinarios == "1":
                        print("SELECT ALL VETERINARIOS")
                        listaveterinarios = Veterinario.SeleccionarVeterinarios()
                        for item in listaveterinarios:
                            print(item.id, item.nombre, item.apellido, item.DNI, item.sueldo)

                    elif opcion_select_veterinarios == "2":
                        print("SELECT POR ID VETERINARIOS")
                        error = False
                        veterinario_a_seleccionar = input("Ingrese el veterinario a seleccionar")
                        try:
                            veterinario = Veterinario.SeleccionarVeterinariosPorID(veterinario_a_seleccionar)
                        except IndexError:
                            print("Usuario no existente")
                        if error == False:
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
            print("INSERT MASCOTAS")
            Menu.MenuFunciones()
            opcion_mascotas = input("Elija la funcion")
            if opcion_mascotas == "1":
                while (1):
                    print("INSERT MASCOTAS")
                    mascota = Mascota()
                    nombre = input("Ingrese nombre: ")
                    if nombre == 'Basta':
                        break
                    tipo = input("Ingrese tipo: ")
                    dueno = input("Ingrese dueno: ")
                    mascota.InsertarMascota(nombre, tipo, dueno)
            elif opcion_mascotas == "2":
                print("UPDATE MASCOTAS")
                mascota_a_modificar = input("Ingrese la mascota a modificar: ")
                error = False
                try:
                    mascota = Mascota.SelectMascotaporID(mascota_a_modificar)
                except IndexError:
                    print("Usuario no existente")
                    error = True
                if error == False:
                    nombre = input("Ingrese el nuevo nombre: ")
                    tipo = input("Tipo: ")
                    dueno_id = input("ID de su dueno: ")
                    try:
                        dueno = Dueno.SeleccionarDuenosPorID(dueno_id)
                        error = True
                    except:
                        print("El dueno no existe")
                    if error == False:
                        mascota.SetMascota(nombre, tipo, dueno_id)
                        mascota.UpdateMascota(mascota_a_modificar)
            elif opcion_mascotas == "3":
                print("DELETE MASCOTAS")
                mascota_a_borrar = input("Ingrese la mascota a borrar: ")
                error = False
                try:
                    mascota = Mascota.SelectMascotaporID(mascota_a_borrar)
                except IndexError:
                    error = True
                    print("Usuario no existente")
                if error == False:
                    try:
                        Mascota.DeleteMascota(mascota_a_borrar)
                    except:
                        print("Esta mascota es una clave foranea y por tanto no se puede eliminar")
            elif opcion_mascotas == "4":
                while(loop):
                    Menu.MenuSelects()
                    opcion_select_mascotas = input("Elija la funcion: ")

                    if opcion_select_mascotas == "1":
                        print("SELECT ALL MASCOTAS")
                        listamascotas = Mascota.SelectMascota()
                        for item in listamascotas:
                            print(item.id, item.nombre, item.tipo, item.dueno.id)

                    elif opcion_select_mascotas == "2":
                        print("SELECT POR ID MASCOTAS")
                        error = False
                        mascota_a_seleccionar = input("Ingrese mascotas a seleccionar")
                        try:
                            mascota = Mascota.SelectMascotaporID(mascota_a_seleccionar)
                        except IndexError:
                            print("Usuario no existente")
                            error = True
                        if error == False:
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
            print("CONSULTAS")
            Menu.MenuFunciones()
            opcion_consultas = input("Elija la funcion")

            if opcion_consultas == "1":
                while (loop):
                    print("INSERT CONSULTAS")
                    error = False
                    consulta = Consulta()
                    continuar = input('Desea continuar?: ')
                    if continuar == "Basta":
                        break
                    precio = int(input("Inserte precio: "))
                    masscota = input("Inserte mascota: ")
                    try:
                        Mascota.SelectMascotaporID(masscota)
                    except IndexError:
                        print("La mascota no existe")
                        error = True
                    if error == False:
                        diagnos = input("Inserte diagnostico: ")
                        vet = input("Inserte veterinario: ")
                        try:
                            Veterinario.SeleccionarVeterinariosPorID(vet)
                        except IndexError:
                            print("El veterinario no existe")
                            error = True
                        if error == False:
                            consulta.InsertarConsulta(precio, diagnos, masscota, vet)
            elif opcion_consultas == "2":
                print("UPDATE CONSULTAS")
                consulta_a_modificar = input("Ingrese la consulta a modificar: ")
                error = False
                try:
                    consulta = Consulta.SelectConsultasPorID(consulta_a_modificar)
                except IndexError:
                    print("Consulta no existente")
                    error = True
                if error == False:
                    precio = input("Ingrese el precio nuevo: ")
                    diagnostico = input("Diagnostico: ")

                    masscota = input("ID de la mascota: ")
                    try:
                        Mascota.SelectMascotaporID(masscota)
                    except IndexError:
                        print("La mascota no existe")
                        error = True
                    if error == False:
                        veterinario = input("ID del veterinario: ")
                        try:
                            Mascota.SelectMascotaporID(masscota)
                        except IndexError:
                            print("La mascota no existe")
                            error = True
                        if error == False:
                            consulta.SetConsulta(precio, diagnostico, masscota, veterinario)
                            consulta.UpdateConsulta(consulta_a_modificar)
            elif opcion_consultas == "3":
                print("DELETE CONSULTAS")
                consulta_a_borrar = input("Ingrese la consulta a borrar: ")
                error = False
                try:
                    consulta = Consulta.SelectConsultasPorID(consulta_a_borrar)
                except IndexError:
                    print("Consulta no existente")
                    error = True
                if error == False:
                    try:
                        Consulta.DeleteConsulta(consulta_a_borrar)
                    except:
                        print("Esta consulta es una clave foranea y por tanto no se puede eliminar")
            elif opcion_consultas == "4":
                while(loop):
                    Menu.MenuSelects()
                    opcion_select_consultas = input("Elija la funcion: ")
                    if opcion_select_consultas == "1":
                        print("SELECT ALL CONSULTAS")
                        listaconsultas = Consulta.SelectConsultas()
                        for item in listaconsultas:
                            print(item.id, item.precio, item.diagnostico, item.mascota.id, item.veterinario.id)

                    elif opcion_select_consultas == "2":
                        print("SELECT POR ID CONSULTAS")
                        error = False
                        consulta_a_seleccionar = input("Ingrese la consulta a seleccionar")
                        try:
                            consulta = Consulta.SelectConsultasPorID(consulta_a_seleccionar)
                        except IndexError:
                            print("Consulta no existente")
                            error = True
                        if error == False:
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
