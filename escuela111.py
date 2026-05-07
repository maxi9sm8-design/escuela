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

cursos_lista = list(colegio.keys())

while True:
    print("BIENVENIDO A LA PAGINA DEL LICEO PEPITOS XD")
    print("seleccione su rol:")
    print("1. Administrador")
    print("2. Estudiante")
    print("3. Salir del programa")
    
    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            clave = input("Contraseña de admin: ")
            if clave == "python":
                print("Menu administrador ")
                print("1. Registrar Alumno")
                print("2. Ver Registro ")
                admin_op = input("Seleccione: ")

                match admin_op:
                    case "1":
                        print("REGISTRO DE ALUMNOS")
                        while True:
                            rut_nuevo = input("Ingresar rut (números o letra k , 7-9 caracteres): ")
                            if len(rut_nuevo) >= 7 and len(rut_nuevo) <= 9:
                                if all(c.isdigit() or c.lower() == "k" for c in rut_nuevo):
                                    break
                            print("El rut debe contener solo números o la letra 'k', y tener 7 a 9 caracteres")

                        if any(rut_nuevo in colegio[cur] for cur in colegio):
                            print("Este rut ya está en el sistema.")
                        else:
                            while True:
                                nom = input("Nombre (solo letras, mín. 2): ")
                                if nom.isalpha() and len(nom) >= 2:
                                    break
                                print("El nombre debe tener solo letras y al menos 2 caracteres.")

                            while True:
                                ape = input("Apellido paterno (mín. 2): ")
                                if len(ape) >= 2:
                                    break
                                print("El apellido debe tener al menos 2 caracteres.")

                            while True:
                                ape2 = input("Apellido materno (mín. 2): ")
                                if len(ape2) >= 2:
                                    ape_completo = ape + " " + ape2
                                    break
                                print("El apellido debe tener al menos 2 caracteres.")

                            print("Seleccione tipo de enseñanza:")
                            print("1. Básica")
                            print("2. Media")
                            tipo = input("Opción: ")
                            
                            curso_final = ""
                            match tipo:
                                case "1":
                                    for i, nombre_c in enumerate(cursos_lista[:8]):
                                        print(i + 1, ".", nombre_c)
                                    n = input("Número de curso: ")
                                    if n.isdigit() and int(n) >= 1 and int(n) <= 8:
                                        curso_final = cursos_lista[int(n)-1]
                                case "2":
                                    for i, nombre_c in enumerate(cursos_lista[8:]):
                                        print(i + 1, ".", nombre_c)
                                    n = input("Número de curso: ")
                                    if n.isdigit() and int(n) >= 1 and int(n) <= 4:
                                        curso_final = cursos_lista[7 + int(n)]

                            if curso_final != "":
                                colegio[curso_final][rut_nuevo] = Alumno(rut_nuevo, nom, ape_completo, curso_final)
                                print("Alumno", nom, "guardado con éxito.")
                            else:
                                print("Opción no válida.")

                    case "2":
                        print("Registro de alumnos:")
                        total = sum(len(colegio[c]) for c in colegio)
                        if total == 0:
                            print("(Sin alumnos)")
                        
                        for c in colegio:
                            print("Curso:", c)
                            for r in colegio[c]:
                                al = colegio[c][r]
                                print("RUT:", r, "| Nombre:", al.nombre, al.apellido)
            else:
                print("Acceso denegado.")

        case "2":
            rut_login = input("Ingrese su rut: ")
            alumno_entrar = None
            for c in colegio:
                if rut_login in colegio[c]:
                    alumno_entrar = colegio[c][rut_login]
            
            if alumno_entrar:
                if alumno_entrar.password == None:
                    print("Hola", alumno_entrar.nombre, "crea tu clave.")
                    while True:
                        c1 = input("Nueva clave: ")
                        c2 = input("Confirme clave: ")
                        if c1 == c2 and len(c1) > 0:
                            alumno_entrar.password = c1
                            print("Clave establecida.")
                            break
                        print("Las claves no coinciden.")
                
                intento = input("Ingrese su clave: ")
                if intento == alumno_entrar.password:
                    print("Bienvenido", alumno_entrar.nombre)
                    while True:
                        print("MENU ESTUDIANTES\n1. Hacer tarea\n2. Estudiar\n3. Generar certificado\n4. Salir")
                        est_op = input("Opción: ")
                        match est_op:
                            case "1": print("haz tarea vago/a")
                            case "2": print("que esperas bobo/a")
                            case "3":
                                if input("Clave: ") == alumno_entrar.password:
                                    print("--------------------------------------------")
                                    print("Certificado de", alumno_entrar.nombre, alumno_entrar.apellido)
                                    print("Curso:", alumno_entrar.curso)
                                    print("--------------------------------------------")
                                else: print("Clave incorrecta.")
                            case "4": break
                            case _: print("Opción no válida.")
                else: print("Clave incorrecta.")
            else: print("RUT no registrado.")

        case "3":
            print("Cerrando el programa de Pepitos XD...")
            break
        case _:
            print("Opción no válida.")