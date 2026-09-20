#!/usr/bin/python3
"""Create classes for each table."""


class Member:
    """Represent table members."""

    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email

    def __str__(self):
        """Display of the members."""
        return "{}: {} ({})".format(
                self.member_id, self.name, self.email
            )

class Equipment:
    """Represent table equipment."""

    def __init__(self, equipment_id, name, category, quantity, available):
        self.equipment_id = equipment_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.available = available

    def is_available(self):
        """Return whether equipment is available."""
        return self.available == 1

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

    def is_active(self):
        """Checks if the loan has not yet been returned."""
        return self.return_date is None

    def __str__(self):
        """Display of loan."""
        status = "Active" if self.is_active() else "Returned"

        return "{}: Member {} borrowed Equipment {} - {}".format(
                self.loan_id,
                self.member_id,
                self.equipment_id,
                status
            )
