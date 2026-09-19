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
