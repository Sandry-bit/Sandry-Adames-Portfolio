from request_manager import menu_solicitudes
from history_manager import mostrar_historial
from database import (
    initialize_database,
    update_old_task_types
)

def mostrar_comandos():
    """Muestra los comandos disponibles."""

    print("\n--- COMANDOS DISPONIBLES ---")
    print("Resume: texto")
    print("Corrige: texto")
    print("Traduce al inglés: texto")
    print("Genera un título: texto")

    input("\nPresiona Enter para volver al menú...")

def main():
    print("=================================")
    print("       AUTOMATIZADOR IA")
    print("=================================")

    initialize_database()
    update_old_task_types()

    while True:
        print("1. Procesar una solicitud")
        print("2. Ver historial")
        print("3. Ver comandos disponibles")
        print("4. Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            menu_solicitudes()

        elif opcion == "2":
            mostrar_historial()

        elif opcion == "3":
            mostrar_comandos()

        elif opcion == "4":
            print("\n👋 Cerrando Automatizador IA...")
            break

        else:
            print("\n❌ Opción no válida.")


if __name__ == "__main__":
    main()