from Clase_DB import DB

class Veterinario(object):
    id = None
    nombre = None
    apellido = None
    DNI = None
    sueldo = None

    def SetVeterinario(self, nombre, apellido, DNI, sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
        self.sueldo = sueldo

    def DeserializarVeterinario(self, diccionario_veterinarios):
        self.id = diccionario_veterinarios['id_veterinario']
        self.nombre = diccionario_veterinarios['nombre']
        self.apellido = diccionario_veterinarios['apellido']
        self.DNI = diccionario_veterinarios['DNI']
        self.sueldo = diccionario_veterinarios['sueldo']

    def InsertarVeterinario(self, nombre, apellido, Dni, sueldo):
        self.SetVeterinario(nombre, apellido, Dni, sueldo)
        DB().run("INSERT INTO Veterinarios values(null,'" + self.nombre + "','" + self.apellido + "'," + str(self.DNI) + "," + str(self.sueldo) + ");")

    @staticmethod
    def SeleccionarVeterinarios():
        lista = []
        select_cursor = DB().run("Select * from Veterinarios;")
        for item in select_cursor:
            veterinariox = Veterinario()
            veterinariox.DeserializarVeterinario(item)
            lista.append(veterinariox)
        return lista

    @staticmethod
    def SeleccionarVeterinariosPorID(id):
        select_cursor = DB().run("Select * from Veterinarios where id_veterinario = " + str(id) + ";")
        d = select_cursor.fetchall()
        veterinario = Veterinario()
        veterinario.DeserializarVeterinario(d[0])
        return veterinario

    @staticmethod
    def BuscarVeterinario(id):
        vt = Veterinario()
        listaa = vt.SeleccionarVeterinarios()
        for item in listaa:
            if item == id:
                return item

    def UpdateVeterinario(self, id):
        DB().run("Update Veterinarios set nombre = '" + self.nombre + "', apellido = '" + self.apellido + "', DNI = " + str(self.DNI) +", sueldo = " + str(self.sueldo) + ", id_veterinario = " + str(self.id) + " where id_veterinario = " + str(id) + ";")

    def DeleteVeterinario(self, id):
        DB().run("Delete from Veterinarios where id_veterinario = " + str(id) + ";")