#!/usr/bin/python3
"""Contains SQLite connection, schema creation, and SQL helpers."""

import sqlite3


def create_tables():
    # Creates a tables if they do not exist in the database makerspace
    connection = sqlite3.connect("makerspace.db")
    
    cursor = connection.cursor()
    
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS members (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
            """)
    
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS equipment (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                available INTEGER NOT NULL DEFAULT 1
            )
            """)
    
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS loans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                member_id INTEGER NOT NULL,
                equipment_id INTEGER NOT NULL,
                checkout_date TEXT NOT NULL,
                return_date TEXT,
                FOREIGN KEY (member_id) REFERENCES members(id),
                FOREIGN KEY (equipment_id) REFERENCES equipment(id)
            )
            """)
    
    connection.commit()
    connection.close()

def add_member(name, email):
    """Add a new member to the database."""
    connection = sqlite3.connect("makerspace.db")
    cursor = connection.cursor()

    cursor.execute(
            "INSERT INTO members (name, email) VALUES (?, ?)",
            (name, email)
        )

    connection.commit()
    member_id = cursor.lastrowid
    connection.close()

    return member_id

def get_members():
    """Return all the members from the database."""
    connection = sqlite3.connect("makerspace.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM members")
    members = cursor.fetchall()

    connection.close()

    return members

def update_member(member_id, name, email):
    """Update a member's name and email."""
    connection = sqlite3.connect("makerspace.db")
    cursor = connection.cursor()

    cursor.execute(
            """
            UPDATE members
            SET name = ?, email = ?
            WHERE id = ?
            """,
            (name, email, member_id)
        )

    connection.commit()

    updated = cursor.rowcount

    connection.close()

    return updated

def delete_member(member_id):
    """Delete a member from the database."""
    connection = sqlite3.connect("makerspace.db")
    cursor = connection.cursor()

    cursor.execute(
            "DELETE FROM members WHERE id = ?",
            (member_id,)
        )

    connection.commit()

    deleted = cursor.rowcount

    connection.close()

    return deleted

def add_equipment(name, category, available=1):
    """Add new equipment to the database."""
    connection = sqlite3.connect("makerspace.db")
    cursor = connection.cursor()

    cursor.execute(
            """
            INSERT INTO equipment (name, category, available)
            VALUES (?, ?, ?)
            """,
            (name, category, available)
        )

    connection.commit()

    equipment_id = cursor.lastrowid

    connection.close()
    
    return equipment_id

def get_equipment():
    """Return all the equipment from database."""

    connection = sqlite3.connect("makerspace.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM equipment")
    equipment = cursor.fetchall()

    connection.close()

    return equipment

def update_equipment(equipment_id, name, category, available=1):
    """Update an equipment's name, category and availability."""
    connection = sqlite3.connect("makerspace.db")
    cursor = connection.cursor()

    cursor.execute(
            """
            UPDATE equipment
            SET name = ?, category = ?, available = ?
            WHERE id = ?
            """,
            (name, category, available, equipment_id)
        )

    connection.commit()
    updated = cursor.rowcount
    connection.close
    return updated

def delete_equipment(equipment_id):
    """Delete equipment from database."""
    connection = sqlite3.connect("makerspace.db")
    cursor = connection.cursor()

    cursor.execute(
            "DELETE FROM equipment WHERE id = ?",
            (equipment_id,)
        )
    connection.commit()
    deleted = cursor.rowcount
    connection.close()
    return deleted

if __name__ == "__main__":
    print(get_equipment())
    name = input("name:")
    category = input("category:")
    add_equipment(name, category)
    print(get_equipment())
    equipment_id = input("equipment_id:")
    delete_equipment(equipment_id)
    print(get_equipment())
