
📖 Descripción del Proyecto
¿Qué es?
Este proyecto es una plataforma de gestión académica basada en consola, desarrollada en Python.
El sistema actúa como un backend administrativo que permite el control de flujos de datos escolares, desde el registro de usuarios hasta la emisión de documentos oficiales,
utilizando el paradigma de Programación Orientada a Objetos (POO).

¿Para qué sirve?
El software está diseñado para resolver tres necesidades fundamentales en la administración educativa:

Gestión Centralizada de Información: Utiliza una estructura de datos jerárquica (diccionarios anidados)
para organizar a los estudiantes por niveles de enseñanza (Básica y Media), permitiendo un acceso rápido y ordenado a los registros.

Validación Robusta de Identidad: Implementa algoritmos de filtrado para capturar datos precisos. Soporta formatos específicos de identificación
(RUT con números y dígito verificador 'k') y permite el ingreso de nombres y apellidos complejos con espacios, evitando errores en la base de datos.

Sistema de Autogestión Segura: Proporciona un entorno de login donde el estudiante es responsable de su propia seguridad. 
Permite la creación de credenciales personalizadas y la generación automática de certificados de alumno regular mediante re-autenticación.


Shutterstock
Explorar
🛠️ Aspectos Técnicos Destacados
Modelado de Datos: Uso de clases para encapsular la información del alumno, facilitando la escalabilidad del sistema.

Lógica de Control: Implementación de la sentencia match-case (Python 3.10+) para un manejo de menús más eficiente y legible.

Sanitización de Inputs: Procesamiento de cadenas de texto para estandarizar entradas
(conversión a minúsculas, eliminación de espacios innecesarios y validación alfanumérica).
