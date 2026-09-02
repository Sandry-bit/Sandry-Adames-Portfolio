from database import (
    get_tasks,
    search_tasks,
    get_tasks_by_type,
    get_task_by_id,
    get_task_statistics
)


def mostrar_resumen_tarea(task):
    """Muestra la información resumida de una tarea."""

    print(f"\nID: {task[0]}")
    print(f"Tipo: {task[3]}")
    print(f"Entrada: {task[1]}")
    print(f"Fecha: {task[4]}")


def filtrar_por_tipo():
    """Muestra las tareas filtradas por tipo."""

    print("\n--- FILTRAR POR TIPO ---")
    print("1. Resumen")
    print("2. Corrección")
    print("3. Traducción al inglés")
    print("4. Generación de título")

    opcion = input("\nSelecciona un tipo: ")

    tipos = {
        "1": "Resumen",
        "2": "Corrección",
        "3": "Traducción al inglés",
        "4": "Generación de título"
    }

    if opcion not in tipos:
        print("\n❌ Opción no válida.")
        input("\nPresiona Enter para volver al historial...")
        return

    task_type = tipos[opcion]

    tasks = get_tasks_by_type(task_type)

    print(f"\n--- TAREAS: {task_type.upper()} ---")

    if not tasks:
        print("No hay tareas de este tipo.")
    else:
        for task in tasks:
            print(f"\nID: {task[0]}")
            print(f"Entrada: {task[1]}")
            print(f"Respuesta: {task[2]}")
            print(f"Tipo: {task[3]}")
            print(f"Fecha: {task[4]}")

    input("\nPresiona Enter para volver al historial...")

def mostrar_detalles_tarea():
    """Busca una tarea por ID y muestra todos sus detalles."""

    task_id = input("\nEscribe el ID de la tarea: ")

    if not task_id.isdigit():
        print("\n❌ El ID debe ser un número.")
        input("\nPresiona Enter para continuar...")
        return

    task = get_task_by_id(int(task_id))

    if not task:
        print("\n❌ No existe una tarea con ese ID.")
        input("\nPresiona Enter para continuar...")
        return

    print("\n--- DETALLES DE LA TAREA ---")
    print(f"\nID: {task[0]}")
    print(f"Tipo: {task[3]}")
    print(f"Fecha: {task[4]}")

    print("\nEntrada:")
    print(task[1])

    print("\nRespuesta:")
    print(task[2])

    input("\nPresiona Enter para continuar...")

def mostrar_estadisticas():
    """Muestra estadísticas de las tareas guardadas."""

    statistics = get_task_statistics()

    print("\n--- ESTADÍSTICAS ---")

    if not statistics:
        print("\nNo hay tareas registradas.")
    else:
        total = sum(count for task_type, count in statistics)

        print(f"\nTotal de tareas: {total}")

        for task_type, count in statistics:
            print(f"{task_type}: {count}")

    input("\nPresiona Enter para volver al historial...")

def mostrar_historial():
    """Muestra el menú del historial."""

    while True:
        print("\n--- HISTORIAL ---")
        print("1. Ver todas las tareas")
        print("2. Buscar una tarea")
        print("3. Filtrar por tipo")
        print("4. Ver detalles de una tarea")
        print("5. Ver estadísticas")
        print("6. Volver al menú principal")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            tasks = get_tasks()

            print("\n--- TODAS LAS TAREAS ---")

            if not tasks:
                print("No hay tareas guardadas.")
            else:
                for task in tasks:
                    mostrar_resumen_tarea(task)

            input("\nPresiona Enter para volver al historial...")

        elif opcion == "2":
            search_text = input("\nEscribe qué quieres buscar: ")

            if not search_text.strip():
                print("\n❌ La búsqueda no puede estar vacía.")
                continue

            tasks = search_tasks(search_text)

            print("\n--- RESULTADOS DE BÚSQUEDA ---")

            if not tasks:
                print("No se encontraron tareas.")
            else:
                for task in tasks:
                    print(f"\nID: {task[0]}")
                    print(f"Entrada: {task[1]}")
                    print(f"Respuesta: {task[2]}")
                    print(f"Tipo: {task[3]}")
                    print(f"Fecha: {task[4]}")

            input("\nPresiona Enter para volver al historial...")

        elif opcion == "3":
            filtrar_por_tipo()

        elif opcion == "4":
            mostrar_detalles_tarea()

        elif opcion == "5":
            mostrar_estadisticas()

        elif opcion == "6":
            break

        else:
            print("\n❌ Opción no válida.")