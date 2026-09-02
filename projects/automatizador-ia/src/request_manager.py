from task_manager import ejecutar_solicitud


def menu_solicitudes():
    """Muestra el menú de tipos de solicitudes."""

    while True:
        print("\n--- PROCESAR SOLICITUD ---")
        print("1. Resumir texto")
        print("2. Corregir texto")
        print("3. Traducir al inglés")
        print("4. Generar título")
        print("5. Volver al menú principal")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            ejecutar_solicitud(
                "Resume: ",
                "Escribe el texto que quieres resumir",
                "Resumen"
            )

        elif opcion == "2":
            ejecutar_solicitud(
                "Corrige: ",
                "Escribe el texto que quieres corregir",
                "Corrección"
            )

        elif opcion == "3":
            ejecutar_solicitud(
                "Traduce al inglés: ",
                "Escribe el texto que quieres traducir",
                "Traducción al inglés"
            )

        elif opcion == "4":
            ejecutar_solicitud(
                "Genera un título: ",
                "Escribe el texto para generar el título",
                "Generación de título"
            )

        elif opcion == "5":
            break

        else:
            print("\n❌ Opción no válida.")