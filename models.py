#!/usr/bin/python3
from database import get_connection
import sqlite3

"""Create classes for each table."""


class Member:
    """Represent table members."""

    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
    
    def save(self):
        """Add data to database."""
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                    """
                    INSERT INTO members (name, email)
                    VALUES (?, ?)
                    """,
                    (self.name, self.email)
                )
            connection.commit()
            self.member_id = cursor.lastrowid
            return self.member_id

        except sqlite3.IntegrityError:
            connection.rollback()
            return False

        finally:
            connection.close()

    @classmethod
    def get_all(cls):
        """Return all members from the database."""
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM members")
        rows = cursor.fetchall()

        connection.close()

        members = []

        for row in rows:
            member = cls(row[0], row[1], row[2])
            members.append(member)
        return members

    def update(self, name, email):
        """Update this member in the database."""
        connection = get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute(
                """
                UPDATE members
                SET name = ?, email = ?
                WHERE id = ?
                """,
                (name, email, self.member_id)
            )

            connection.commit()
            updated = cursor.rowcount

            if updated:
                self.name = name
                self.email = email

            return updated
        except sqlite3.IntegrityError:
            connection.rollback()
            return False

        finally:
            connection.close()

    def delete(self):
        """Delete this member from the database."""
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM members WHERE id = ?",
            (self.member_id,)
        )

        connection.commit()
        deleted = cursor.rowcount
        connection.close()

        return deleted

    @classmethod
    def search_by_id(cls, member_id):
        """Search for a member by ID."""
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM members WHERE id = ?",
            (member_id,)
        )

        row = cursor.fetchone()
        connection.close()

        if row is None:
            return None

        return cls(row[0], row[1], row[2])

    @classmethod
    def search_by_name(cls, name):
        """Search for members by name."""
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM members WHERE name LIKE ?",
            ("%" + name + "%",)
        )

        rows = cursor.fetchall()
        connection.close()

        members = []

        for row in rows:
            members.append(cls(row[0], row[1], row[2]))

        return members

    @classmethod
    def search_by_email(cls, email):
        """Search for members by email."""
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
                "SELECT * FROM members WHERE email LIKE ?",
            ("%" + email + "%",)
        )

        rows = cursor.fetchall()
        connection.close()

        members = []

        for row in rows:
            members.append(cls(row[0], row[1], row[2]))

        return members

    def __str__(self):
        """Display of the members."""
        return "{}: {} ({})".format(
                self.member_id,
                self.name,
                self.email
            )

class Equipment:
    """Represent table equipment."""

    def __init__(self, equipment_id, name, category, quantity, available):
        self.equipment_id = equipment_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.available = available

    def save(self):
        """Save this equipment to the database."""
        connection = get_connection()
        cursor = connection.cursor()

        available = 1 if self.quantity > 0 else 0

        cursor.execute(
            """
            INSERT INTO equipment (name, category, quantity, available)
            VALUES (?, ?, ?, ?)
            """,
            (self.name, self.category, self.quantity, available)
        )

        connection.commit()
        self.equipment_id = cursor.lastrowid
        self.available = available
        connection.close()

        return self.equipment_id

    @classmethod
    def get_all(cls):
        """Return all equipment from the database."""
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM equipment")
        rows = cursor.fetchall()

        connection.close()

        equipment_list = []

        for row in rows:
            equipment = cls(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4]
            )
            equipment_list.append(equipment)

        return equipment_list

    def update(self, name, category, quantity):
        """Update this equipment in the database."""
        connection = get_connection()
        cursor = connection.cursor()

        available = 1 if quantity > 0 else 0

        cursor.execute(
            """
            UPDATE equipment
            SET name = ?, category = ?, quantity = ?, available = ?
            WHERE id = ?
            """,
            (
                name,
                category,
                quantity,
                available,
                self.equipment_id
            )
        )

        connection.commit()
        updated = cursor.rowcount
        connection.close()

        if updated:
            self.name = name
            self.category = category
            self.quantity = quantity
            self.available = available

        return updated

    def delete(self):
        """Delete this equipment from the database."""
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM equipment WHERE id = ?",
            (self.equipment_id,)
        )

        connection.commit()
        deleted = cursor.rowcount
        connection.close()

        return deleted

    def is_available(self):
        """Return whether equipment is available."""
        return self.available == 1

    @classmethod
    def search_by_id(cls, equipment_id):
        """Search for equipment by ID."""
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM equipment WHERE id = ?",
            (equipment_id,)
        )

        row = cursor.fetchone()
        connection.close()

        if row is None:
            return None

        return cls(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4]
        )


    @classmethod
    def search_by_name(cls, name):
        """Search for equipment by name."""
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM equipment WHERE name LIKE ?",
            ("%" + name + "%",)
        )

        rows = cursor.fetchall()
        connection.close()

        equipment_list = []

        for row in rows:
            equipment_list.append(
                cls(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4]
                )
            )

        return equipment_list

    @classmethod
    def search_by_category(cls, category):
        """Search for equipment by category."""
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM equipment WHERE category LIKE ?",
            ("%" + category + "%",)
        )

        rows = cursor.fetchall()
        connection.close()

        equipment_list = []

        for row in rows:
            equipment_list.append(
                cls(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4]
                )
            )

        return equipment_list

    def __str__(self):
        """Display of equipment."""
        return "{}: {} ({}) - {} available".format(
                self.equipment_id,
                self.name,
                self.category,
                self.quantity
            )

class Loan:
    """Represent table loans."""

    def __init__(
            self,
            loan_id,
            member_id,
            equipment_id,
            checkout_date,
            return_date
        ):
        self.loan_id = loan_id
        self.member_id = member_id
        self.equipment_id = equipment_id
        self.checkout_date = checkout_date
        self.return_date = return_date

    def save(self):
        """Save this loan to the database."""
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT id FROM members WHERE id = ?",
            (self.member_id,)
        )

        if cursor.fetchone() is None:
            connection.close()
            return False

        cursor.execute(
            """
            SELECT quantity
            FROM equipment
            WHERE id = ?
            """,
            (self.equipment_id,)
        )

        equipment = cursor.fetchone()

        if equipment is None or equipment[0] <= 0:
            connection.close()
            return False

        cursor.execute(
            """
            INSERT INTO loans
            (member_id, equipment_id, checkout_date, return_date)
            VALUES (?, ?, ?, ?)
            """,
            (
                self.member_id,
                self.equipment_id,
                self.checkout_date,
                self.return_date
            )
        )

        self.loan_id = cursor.lastrowid

        cursor.execute(
            """
            UPDATE equipment
            SET quantity = quantity - 1
            WHERE id = ?
            """,
            (self.equipment_id,)
        )

        cursor.execute(
            """
            UPDATE equipment
            SET available = CASE
                WHEN quantity = 0 THEN 0
                ELSE 1
            END
            WHERE id = ?
            """,
            (self.equipment_id,)
        )

        connection.commit()
        connection.close()

        return True

    @classmethod
    def get_all(cls):
        """Return all loans from the database."""
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM loans")
        rows = cursor.fetchall()

        connection.close()

        loans = []

        for row in rows:
            loan = cls(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4]
            )
            loans.append(loan)

        return loans

    def return_loan(self, return_date):
        """Return the equipment and update the loan."""
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT equipment_id, return_date
            FROM loans
            WHERE id = ?
            """,
            (self.loan_id,)
        )

        loan = cursor.fetchone()

        if loan is None:
            connection.close()
            return False

        equipment_id, existing_return_date = loan

        if existing_return_date is not None:
            connection.close()
            return False

        cursor.execute(
            """
            UPDATE loans
            SET return_date = ?
            WHERE id = ?
            """,
            (return_date, self.loan_id)
        )

        cursor.execute(
            """
            UPDATE equipment
            SET quantity = quantity + 1,
                available = 1
            WHERE id = ?
            """,
            (equipment_id,)
        )

        connection.commit()
        connection.close()

        self.return_date = return_date

        return True

    def is_active(self):
        """Checks if the loan has not yet been returned."""
        return self.return_date is None
    
    @classmethod
    def search_by_id(cls, loan_id):
        """Search for a loan by ID."""
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM loans WHERE id = ?",
            (loan_id,)
        )

        row = cursor.fetchone()
        connection.close()

        if row is None:
            return None

        return cls(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4]
        )

    @classmethod
    def search_by_checkout_date(cls, checkout_date):
        """Search for loans by checkout date."""
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM loans WHERE checkout_date = ?",
            (checkout_date,)
        )

        rows = cursor.fetchall()
        connection.close()

        loans = []

        for row in rows:
            loans.append(
                cls(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4]
                )
            )

        return loans

    @classmethod
    def search_by_return_date(cls, return_date):
        """Search for loans by return date."""
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM loans WHERE return_date = ?",
            (return_date,)
        )

        rows = cursor.fetchall()
        connection.close()

        loans = []

        for row in rows:
            loans.append(
                cls(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4]
                )
            )

        return loans

    @classmethod
    def search_by_member_id(cls, member_id):
        """Search for loans by member ID."""
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM loans WHERE member_id = ?",
            (member_id,)
        )

        rows = cursor.fetchall()
        connection.close()

        loans = []

        for row in rows:
            loans.append(
                cls(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4]
                )
            )

        return loans

    @classmethod
    def search_by_equipment_id(cls, equipment_id):
        """Search for loans by equipment ID."""
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM loans WHERE equipment_id = ?",
            (equipment_id,)
        )

        rows = cursor.fetchall()
        connection.close()

        loans = []

        for row in rows:
            loans.append(
                cls(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4]
                )
            )

        return loans

    @classmethod
    def current_loans(cls):
        """Return all current loans."""
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM loans
            WHERE return_date IS NULL
            """
        )

        rows = cursor.fetchall()
        connection.close()

        loans = []

        for row in rows:
            loans.append(
                cls(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4]
                )
            )

        return loans

    @classmethod
    def member_history(cls, member_id):
        """Return all loans for a member."""
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM loans
            WHERE member_id = ?
            """,
            (member_id,)
        )

        rows = cursor.fetchall()
        connection.close()

        loans = []

        for row in rows:
            loans.append(
                cls(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4]
                )
            )

        return loans
    
    @classmethod
    def equipment_history(cls, equipment_id):
        """Return all loans for an equipment item."""
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM loans
            WHERE equipment_id = ?
            """,
            (equipment_id,)
        )

        rows = cursor.fetchall()
        connection.close()

        loans = []

        for row in rows:
            loans.append(
                cls(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4]
                )
            )

        return loans

    def __str__(self):
        """Display of loan."""
        status = "Active" if self.is_active() else "Returned"

        return "{}: Member {} borrowed Equipment {} - {}".format(
                self.loan_id,
                self.member_id,
                self.equipment_id,
                status
            )
