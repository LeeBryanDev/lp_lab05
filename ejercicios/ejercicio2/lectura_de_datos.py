# lectura_de_datos.py

class Persona:
    def __init__(self, nombre, apellido, usuario, contrasena):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.contrasena = contrasena

class Empresa:
    def __init__(self, nombre, ruc, usuario, contrasena):
        self.nombre = nombre
        self.ruc = ruc
        self.usuario = usuario
        self.contrasena = contrasena


# Listas donde se cargarán los usuarios del archivo
personas = []
empresas = []

# Leer el archivo de texto y cargar la información en las listas
with open("actividad3/usuarios.txt", "r", encoding="utf-8") as f:
    for linea in f:
        linea = linea.strip()
        if linea == "":
            continue
        partes = linea.split(",")
        tipo = partes[0]

        if tipo == "persona":
            # persona,nombre,apellido,usuario,contrasena
            p = Persona(partes[1], partes[2], partes[3], partes[4])
            personas.append(p)
        elif tipo == "empresa":
            # empresa,nombre,ruc,usuario,contrasena
            e = Empresa(partes[1], partes[2], partes[3], partes[4])
            empresas.append(e)

print("Usuarios cargados correctamente.")
print("Personas:", len(personas), "| Empresas:", len(empresas))

# Pedir usuario y contraseña
usuario_ingresado = input("Ingrese su usuario: ")
contrasena_ingresada = input("Ingrese su contraseña: ")

# Buscar en las personas
encontrado = False
for p in personas:
    if p.usuario == usuario_ingresado and p.contrasena == contrasena_ingresada:
        print("Ingreso exitoso. Bienvenido/a", p.nombre, p.apellido, "(Persona)")
        encontrado = True

# Buscar en las empresas
for e in empresas:
    if e.usuario == usuario_ingresado and e.contrasena == contrasena_ingresada:
        print("Ingreso exitoso. Bienvenido/a", e.nombre, "(Empresa) - RUC:", e.ruc)
        encontrado = True

if not encontrado:
    print("Usuario o contraseña incorrectos. Acceso denegado.")