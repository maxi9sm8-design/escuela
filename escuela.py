class Alumno:
    def __init__(self, rut, nombre, apellido, curso):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        self.password = None

colegio = {
    "1ero Básico": {}, "2do Básico": {}, "3ero Básico": {}, "4to Básico": {},
    "5to Básico": {}, "6to Básico": {}, "7mo Básico": {}, "8vo Básico": {},
    "1ero Medio": {}, "2do Medio": {}, "3ero Medio": {}, "4to Medio": {}
}

while True:
    print("BIENVENIDO A LA PAGINA DEL LICEO PEPITOS XD")
    print("seleccione su rol:")
    print("1. Administrador")
    print("2. Estudiante")
    print("3. Salir del programa")
    
    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            clave = input("Contraseña de administrador: ").lower()
            if clave == "python":
                print(" Menu administrador ")
                print("1. Registrar Alumno")
                print("2. Ver Registro ")
                admin_op = input("Seleccione: ")

                if admin_op == "1":
                    print(" REGISTRO DE ALUMNOS")
                    rut_nuevo = input("ingresar rut")
                    
                    ya_existe = False
                    for curso in colegio:
                        if rut_nuevo in colegio[curso]:
                            ya_existe = True
                            break
                    
                    if ya_existe:
                        print("Error: Este rut ya está en el sistema.")
                    else:
                        nom = input("Nombre: ")
                        ape = input("Apellido: ")

                        print("Seleccione tipo de enseñanza:")
                        print("1. Básica")
                        print("2. Media")
                        tipo = input("Opción: ")
                        
                        cur = ""
                        match tipo:
                            case "1":
                                print("1. 1ero Básico, 2. 2do Básico, 3. 3ero Básico, 4. 4to Básico")
                                print("5. 5to Básico, 6. 6to Básico, 7. 7mo Básico, 8. 8vo Básico")
                                n = input("Número de curso: ")
                                match n:
                                    case "1": cur = "1ero Básico"
                                    case "2": cur = "2do Básico"
                                    case "3": cur = "3ero Básico"
                                    case "4": cur = "4to Básico"
                                    case "5": cur = "5to Básico"
                                    case "6": cur = "6to Básico"
                                    case "7": cur = "7mo Básico"
                                    case "8": cur = "8vo Básico"
                            case "2":
                                print("1. 1ero Medio, 2. 2do Medio, 3. 3ero Medio, 4. 4to Medio")
                                n = input("Número de curso: ")
                                match n:
                                    case "1": cur = "1ero Medio"
                                    case "2": cur = "2do Medio"
                                    case "3": cur = "3ero Medio"
                                    case "4": cur = "4to Medio"

                        if cur != "":
                            colegio[cur][rut_nuevo] = Alumno(rut_nuevo, nom, ape, cur)
                            print(f"Alumno {nom} guardado con éxito en {cur}.")
                        else:
                            print("Opción o curso no válido.")
                
                elif admin_op == "2":
                    print("registro de alumnos:")
                    for curso, alumnos in colegio.items():
                        print(f"Curso: {curso}")
                        if not alumnos:
                            print("  (Sin alumnos)")
                        for r, obj in alumnos.items():
                            print(f"RUT: {r} | Nombre: {obj.nombre} {obj.apellido}")
            else:
                print("Acceso denegado.")

        case "2":
            Rut = input("Ingrese su RUT: ")
            
            alumno_entrar = None
            for curso in colegio:
                if Rut in colegio[curso]:
                    alumno_entrar = colegio[curso][Rut]
            
            if alumno_entrar:
                if alumno_entrar.password is None:
                    print(f"Hola {alumno_entrar.nombre}, crea tu clave.")
                    while True:
                        c1 = input("Nueva clave: ").lower()
                        c2 = input("Confirme clave: ").lower()
                        if c1 == c2 and c1 != "":
                            alumno_entrar.password = c1
                            print("Clave establecida.")
                            break
                        else:
                            print("La contraseña no coincide")
                
                alumno_intento = input("Ingrese su clave para entrar: ").lower()
                if alumno_intento == alumno_entrar.password:
                    print(f"Bienvenido {alumno_entrar.nombre.upper()} ")
                    
                    while True:
                        print(" MENU ESTUDIANTES ")
                        print("1. Hacer tarea")
                        print("2. Estudiar")
                        print("3. Salir")
                        print("4. certificado")
                        estudiante_op = input("Seleccione una opción: ")
                        
                        match estudiante_op:
                            case "1":
                                print("haz tarea vago/a")
                            case "2":
                                print("que esperas bob/a")
                            case "3":
                                print("Regresando al menú principal...")
                            case "4":
                                print("Generando certificado...")
                                break
                            case _:
                                print("Opción no válida.")
                else:
                    print("Clave incorrecta.")
            else:
                print("RUT no registrado.")

        case "3":
            print("Cerrando el programa de Pepitos XD...")
            break
        
        case _:
            print("Opción no válida.")