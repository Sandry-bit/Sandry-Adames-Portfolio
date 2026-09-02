from ai_processor import process_with_ai
from database import save_task


def ejecutar_solicitud(comando, mensaje, task_type):
    """Procesa una solicitud y guarda el resultado."""

    prompt = input(f"\n{mensaje}: ")

    if not prompt.strip():
        print("\n❌ No puedes dejar el texto vacío.")
        return

    result = process_with_ai(comando + prompt)

    print("\n--- RESPUESTA ---")
    print(result)

    save_task(prompt, result, task_type)
    print("\n✅ Resultado guardado en la base de datos.")

    input("\nPresiona Enter para continuar...")