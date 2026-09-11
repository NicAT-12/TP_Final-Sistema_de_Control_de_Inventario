# Sistema de Control de Inventario — Ferretería

Trabajo Práctico Integrador de **Programación 1** — Tecnicatura Universitaria en Programación a Distancia (TUPaD), UTN.
1° Cuatrimestre 2026.

## Descripción

Una ferretería local necesita digitalizar el control de sus productos para evitar pérdidas de stock. Este programa permite gestionar las herramientas a la venta y sus unidades disponibles en tiempo real, mediante un menú interactivo:

1. Carga de herramientas con existencias iniciales
2. Visualización de inventario
3. Consulta de stock
4. Reporte de agotados
5. Alta de nuevo producto
6. Actualización de stock (venta / ingreso)
7. Salir

## Tecnologías

Python puro, sin librerías externas. Toda la información se maneja con una única lista de diccionarios (`inventario[]`), donde cada elemento tiene las claves `'herramienta'` y `'cantidad'`.

## Cómo ejecutar

*(a completar cuando el código esté integrado)*

## Clonar el repositorio en local

Para obtener una copia del proyecto en tu computadora y poder trabajar con él de forma local, se debe clonar el repositorio desde GitHub.

### 1. Verificar que Git esté instalado

Abrir una terminal y ejecutar:

```bash
git --version
```

Si Git está instalado correctamente, se mostrará su versión, por ejemplo:

```text
git version 2.x.x
```

### 2. Elegir la ubicación del proyecto

Abrir una terminal y dirigirse a la carpeta donde se desea guardar el proyecto.

Por ejemplo:

```bash
cd Documentos
```

También se puede utilizar cualquier otra ubicación de preferencia.

### 3. Clonar el repositorio

Ejecutar el siguiente comando:

```bash
git clone https://github.com/NicAT-12/TP_Final-Sistema_de_Control_de_Inventario.git
```

Este comando descargará el repositorio completo desde GitHub y creará una carpeta llamada:

```text
TP_Final-Sistema_de_Control_de_Inventario
```

El proceso de clonación también descarga el historial de Git y configura automáticamente el repositorio remoto como `origin`.

### 4. Ingresar a la carpeta del proyecto

Una vez finalizada la clonación, ejecutar:

```bash
cd TP_Final-Sistema_de_Control_de_Inventario
```

### 5. Verificar el estado del repositorio

Para comprobar que el repositorio local funciona correctamente:

```bash
git status
```

Debería aparecer información similar a:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

### 6. Verificar la conexión con GitHub

Para comprobar que el repositorio local está vinculado correctamente con el repositorio remoto:

```bash
git remote -v
```

Debería mostrarse:

```text
origin  https://github.com/NicAT-12/TP_Final-Sistema_de_Control_de_Inventario.git (fetch)
origin  https://github.com/NicAT-12/TP_Final-Sistema_de_Control_de_Inventario.git (push)
```

### 7. Obtener cambios posteriores

Si en el futuro se realizan cambios en GitHub y se desea actualizar la copia local, primero ingresar a la carpeta del proyecto:

```bash
cd TP_Final-Sistema_de_Control_de_Inventario
```

Luego ejecutar:

```bash
git pull
```

Esto descarga los cambios del repositorio remoto y los integra en la rama local.

### Resumen

Los comandos principales para clonar el proyecto son:

```bash
cd Documentos

git clone https://github.com/NicAT-12/TP_Final-Sistema_de_Control_de_Inventario.git

cd TP_Final-Sistema_de_Control_de_Inventario

git status
```

A partir de ese momento, el proyecto estará disponible localmente y listo para trabajar con Git.

## Autores

- Federico Barranco
- Nicolás Tissoni

## Estado

🚧 En desarrollo.

## Nota sobre la entrega

La entrega formal del TPI se realiza mediante un archivo `.zip` subido a la plataforma institucional (código + informe PDF). Este repositorio es la herramienta de trabajo del equipo durante el desarrollo.
