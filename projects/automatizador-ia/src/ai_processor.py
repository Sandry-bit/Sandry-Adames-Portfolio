def resumir(texto):
    """Genera un resumen básico del texto."""

    palabras = texto.split()

    if len(palabras) <= 10:
        return texto

    return " ".join(palabras[:10]) + "..."

def corregir(texto):
    """Corrige algunos errores básicos."""

    correcciones = {
        "yo tener": "yo tengo",
        "yo hacer": "yo hago",
        "yo poder": "yo puedo",
        "yo querer": "yo quiero",
        "yo saber": "yo sé",
    }

    texto_corregido = texto

    for error, correccion in correcciones.items():
        texto_corregido = texto_corregido.replace(
            error, correccion
        )

    if texto_corregido:
        texto_corregido = (
            texto_corregido[0].upper()
            + texto_corregido[1:]
        )

    if not texto_corregido.endswith("."):
        texto_corregido += "."

    return texto_corregido

def traducir(texto):
    """Traduce algunas frases básicas al inglés."""

    traducciones = {
        "hola": "hello",
        "hola, ¿cómo estás?": "hello, how are you?",
        "buenos días": "good morning",
        "buenas tardes": "good afternoon",
        "buenas noches": "good night",
        "gracias": "thank you",
        "por favor": "please",
        "te quiero": "I love you",
        "adiós": "goodbye",
    }

    return traducciones.get(
        texto.lower(),
        "[Traducción no disponible para esta frase]"
    )

def generar_titulo(texto):
    """Genera un título básico a partir del texto."""

    texto = texto.strip()

    if not texto:
        return "Sin título"

    return texto.capitalize()

def process_with_ai(prompt):
    """
    Detecta el tipo de solicitud y utiliza la función correspondiente.
    """

    if not prompt.strip():
        return "No se recibió ningún texto."

    prompt = prompt.strip()
    prompt_lower = prompt.lower()

    if prompt_lower.startswith("resume"):
        texto = prompt[len("resume"):].lstrip(" :").strip()
        return "[RESUMEN]\n\n" + resumir(texto)

    elif prompt_lower.startswith("corrige"):
        texto = prompt[len("corrige"):].lstrip(" :").strip()
        return "[CORRECCIÓN]\n\n" + corregir(texto)

    elif prompt_lower.startswith("traduce al inglés"):
        texto = prompt[len("traduce al inglés"):].lstrip(" :").strip()
        return "[TRADUCCIÓN AL INGLÉS]\n\n" + traducir(texto)

    elif prompt_lower.startswith("genera un título"):
        texto = prompt[len("genera un título"):].lstrip(" :").strip()
        return "[GENERACIÓN DE TÍTULO]\n\n" + generar_titulo(texto)

    else:
        return (
            "[SOLICITUD NO RECONOCIDA]\n\n"
            "No reconocí el comando.\n\n"
            "Puedes utilizar:\n"
            "- Resume: texto\n"
            "- Corrige: texto\n"
            "- Traduce al inglés: texto\n"
            "- Genera un título: texto"
        )