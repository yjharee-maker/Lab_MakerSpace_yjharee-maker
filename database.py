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

if __name__ == "__main__":
    create_tables()

    print(get_members())

    member_id = input("member_id:")
    name = input("name:")
    email = input("email:")
    update_member(member_id, name, email)

    print(get_members())
