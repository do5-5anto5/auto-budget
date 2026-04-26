import os
import sqlite3
import sys

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "budget.db")


def get_connection() -> sqlite3.Connection:
    """Get a database connection."""
    connection = sqlite3.connect(DB_PATH, isolation_level=None)
    connection.execute(
        "CREATE TABLE IF NOT EXISTS materials (name TEXT NOT NULL UNIQUE) STRICT"
    )
    return connection

def insert_material(name: str) -> str:
    """Insert a material into the database if it doesn't already exist."""
    try:
        connection = get_connection()
        connection.execute("INSERT INTO materials (name) VALUES (?)", (name,))
        print(f"Material '{name}' inserido.")
        return f'{name} salvo.'
    except sqlite3.IntegrityError:
        print(f"Material '{name}' já existe.")
        return f'{name} já existe.'
    except Exception as e:
        print(f"Erro ao inserir material: {e}")
        return f'Erro ao salvar {name}.'

def get_materials() -> list:
    """Get all materials from the database."""
    connection = get_connection()
    materials = connection.execute("SELECT name FROM materials ORDER BY name")
    return [row[0] for row in materials.fetchall()]

def remove_material(name: str):
    """Remove a material from the database."""
    try:
        connection = get_connection()
        cursor = connection.execute("DELETE FROM materials WHERE name = ?", (name,))
        if cursor.rowcount > 0:
            print(f"Material '{name}' removido.")
            return f'{name} removido.'
        else:
            print(f"Material '{name}' não encontrado.")
            return f'{name} não encontrado.'
    except Exception as e:
        print(f"Erro ao remover material: {e}")
        return f'Erro ao remover {name}.'