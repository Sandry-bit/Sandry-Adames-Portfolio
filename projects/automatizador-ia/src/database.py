import sqlite3
from pathlib import Path


DATABASE_PATH = Path(__file__).parent.parent / "data" / "automatizador.db"


def get_connection():
    """Crea y devuelve una conexión con la base de datos."""
    return sqlite3.connect(DATABASE_PATH)


def initialize_database():
    """Crea y actualiza la estructura de la base de datos."""

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            input_text TEXT NOT NULL,
            output_text TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("PRAGMA table_info(tasks)")
    columns = [column[1] for column in cursor.fetchall()]

    if "task_type" not in columns:
        cursor.execute("""
            ALTER TABLE tasks
            ADD COLUMN task_type TEXT DEFAULT 'Desconocido'
        """)

    connection.commit()
    connection.close()


def save_task(input_text, output_text, task_type):
    """Guarda una tarea y su resultado en la base de datos."""

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO tasks (input_text, output_text, task_type)
        VALUES (?, ?, ?)
        """,
        (input_text, output_text, task_type)
    )

    connection.commit()
    connection.close()

def get_tasks():
    """Obtiene todas las tareas guardadas."""
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, input_text, output_text, task_type, created_at
        FROM tasks
        ORDER BY id DESC
    """)

    tasks = cursor.fetchall()

    connection.close()

    return tasks

def search_tasks(search_text):
    """Busca tareas que contengan un texto específico."""

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, input_text, output_text, task_type, created_at
        FROM tasks
        WHERE input_text LIKE ?
        OR output_text LIKE ?
        ORDER BY id DESC
        """,
        (f"%{search_text}%", f"%{search_text}%")
    )

    tasks = cursor.fetchall()

    connection.close()

    return tasks

def get_tasks_by_type(task_type):
    """Obtiene las tareas de un tipo específico."""

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, input_text, output_text, task_type, created_at
        FROM tasks
        WHERE task_type = ?
        ORDER BY id DESC
        """,
        (task_type,)
    )

    tasks = cursor.fetchall()

    connection.close()

    return tasks

def get_task_by_id(task_id):
    """Obtiene una tarea específica mediante su ID."""

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, input_text, output_text, task_type, created_at
        FROM tasks
        WHERE id = ?
        """,
        (task_id,)
    )

    task = cursor.fetchone()

    connection.close()

    return task

def get_task_statistics():
    """Obtiene la cantidad de tareas agrupadas por tipo."""

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT task_type, COUNT(*)
        FROM tasks
        GROUP BY task_type
        ORDER BY task_type
        """
    )

    statistics = cursor.fetchall()

    connection.close()

    return statistics

def update_old_task_types():
    """Actualiza el tipo de las tareas antiguas."""

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE tasks
        SET task_type = 'Resumen'
        WHERE task_type = 'Desconocido'
        AND LOWER(input_text) LIKE 'resume%'
    """)

    cursor.execute("""
        UPDATE tasks
        SET task_type = 'Corrección'
        WHERE task_type = 'Desconocido'
        AND LOWER(input_text) LIKE 'corrige%'
    """)

    cursor.execute("""
        UPDATE tasks
        SET task_type = 'Traducción al inglés'
        WHERE task_type = 'Desconocido'
        AND LOWER(input_text) LIKE 'traduce al inglés%'
    """)

    cursor.execute("""
        UPDATE tasks
        SET task_type = 'Generación de título'
        WHERE task_type = 'Desconocido'
        AND LOWER(input_text) LIKE 'genera un título%'
    """)

    connection.commit()
    connection.close()