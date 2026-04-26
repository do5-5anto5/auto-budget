import sqlite3
import os
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
        "CREATE TABLE IF NOT EXISTS business (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, logo TEXT, logo_image TEXT) STRICT"
    )
    
    # Add logo_image column if it doesn't exist (for migration)
    try:
        connection.execute("ALTER TABLE business ADD COLUMN logo_image TEXT")
        print("Coluna logo_image adicionada com sucesso.")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            pass  # Column already exists
        else:
            print(f"Erro ao adicionar coluna logo_image: {e}")
    
    return connection


def save_business(name: str = None, phone: str = None, logo: str = None, logo_image: str = None) -> str:
    """Save or update business information. Always updates the first row (id=1)."""
    try:
        connection = get_connection()
        
        # Check if business info exists
        cursor = connection.execute("SELECT id FROM business WHERE id = 1")
        exists = cursor.fetchone()
        
        if exists:
            # Update existing record
            if name is not None:
                connection.execute("UPDATE business SET name = ? WHERE id = 1", (name,))
            if phone is not None:
                connection.execute("UPDATE business SET phone = ? WHERE id = 1", (phone,))
            if logo is not None:
                connection.execute("UPDATE business SET logo = ? WHERE id = 1", (logo,))
            if logo_image is not None:
                connection.execute("UPDATE business SET logo_image = ? WHERE id = 1", (logo_image,))
            print("Informações da empresa atualizadas.")
            return "Informações da empresa atualizadas."
        else:
            # Insert new record
            connection.execute(
                "INSERT INTO business (id, name, phone, logo, logo_image) VALUES (1, ?, ?, ?, ?)",
                (name or "", phone or "", logo or "", logo_image or "")
            )
            print("Informações da empresa salvas.")
            return "Informações da empresa salvas."
            
    except Exception as e:
        print(f"Erro ao salvar informações da empresa: {e}")
        return f"Erro ao salvar informações da empresa."


def get_business() -> dict:
    """Get business information from database."""
    try:
        connection = get_connection()
        cursor = connection.execute("SELECT name, phone, logo, logo_image FROM business WHERE id = 1")
        row = cursor.fetchone()
        
        if row:
            return {
                "name": row[0] or "",
                "phone": row[1] or "",
                "logo": row[2] or "",
                "logo_image": row[3] or ""
            }
        else:
            return {"name": "", "phone": "", "logo": "", "logo_image": ""}
            
    except Exception as e:
        print(f"Erro ao carregar informações da empresa: {e}")
        return {"name": "", "phone": "", "logo": "", "logo_image": ""}


def update_business(name: str = None, phone: str = None, logo: str = None, logo_image: str = None) -> str:
    """Update specific business fields."""
    return save_business(name, phone, logo, logo_image)


def clear_business() -> str:
    """Clear all business information."""
    try:
        connection = get_connection()
        connection.execute("DELETE FROM business WHERE id = 1")
        print("Informações da empresa limpas.")
        return "Informações da empresa limpas."
    except Exception as e:
        print(f"Erro ao limpar informações da empresa: {e}")
        return f"Erro ao limpar informações da empresa."

