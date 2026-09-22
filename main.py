#!/usr/bin/python3
"""The main interface of the system."""

from database import create_tables
from models import Member, Equipment, Loan


def main():
    """ Run the system."""
    create_tables()

    while True:
        print("\nMakerspace Checkout System")
        print("\n1. Register member")
        print("2. List members")
        print("3. Update member")
        print("4. Delete member")
        print("\n5. Register equipment")
        print("6. List equipment")
        print("7. Update equipment")
        print("8. Delete equipment")
        print("\n9. Checkout equipment")
        print("10. Return equipment")
        print("\n11. Search")
        print("12. Reports")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "0":
            print("Thank you for using our service! \nGoodBye!")
            break
        elif choice == "1":
            name = input("Enter member name: ")
            email = input("Enter member email: ")

            member = Member(None, name, email)
            member.save()

            print("Member registered successfully.")
            print("Member ID:", member.member_id)
         elif choice == "2":
            members = Member.get_all()

            if not members:
                print("No members found.")
            else:
                for member in members:
                    print(member)
        elif choice == "3":
            member_id = int(input("Enter member ID: "))

            member = Member.search_by_id(member_id)

            if member is None:
                print("Member not found.")
            else:
                name = input("Enter new name: ")
                email = input("Enter new email: ")

                member.update(name, email)

                print("Member updated successfully.")
        elif choice == "4":
            member_id = int(input("Enter member ID: "))

            member = Member.search_by_id(member_id)

            if member is None:
                print("Member not found.")
            else:
                member.delete()
                print("Member deleted successfully.")
        elif choice == "5":
            name = input("Enter equipment name: ")
            category = input("Enter equipment category: ")
            quantity = int(input("Enter quantity: "))

            equipment = Equipment(
                None,
                name,
                category,
                quantity,
                1 if quantity > 0 else 0
            )

            equipment.save()

            print("Equipment registered successfully.")
            print("Equipment ID:", equipment.equipment_id)
        elif choice == "6":
            equipment_list = Equipment.get_all()

            if not equipment_list:
                print("No equipment found.")
            else:
                for equipment in equipment_list:
                    print(equipment)
        elif choice == "7":
            equipment_id = int(input("Enter equipment ID: "))

            equipment = Equipment.search_by_id(equipment_id)

            if equipment is None:
                print("Equipment not found.")
            else:
                name = input("Enter new equipment name: ")
                category = input("Enter new equipment category: ")
                quantity = int(input("Enter new quantity: "))

                equipment.update(name, category, quantity)

                print("Equipment updated successfully.")
        elif choice == "8":
            equipment_id = int(input("Enter equipment ID: "))

            equipment = Equipment.search_by_id(equipment_id)

            if equipment is None:
                print("Equipment not found.")
            else:
                equipment.delete()
                print("Equipment deleted successfully.")
        elif choice == "9":
            member_id = int(input("Enter member ID: "))
            equipment_id = int(input("Enter equipment ID: "))
            checkout_date = input("Enter checkout date: ")

            loan = Loan(
                None,
                member_id,
                equipment_id,
                checkout_date,
                None
            )

            if loan.save():
                print("Equipment checked out successfully.")
                print("Loan ID:", loan.loan_id)
            else:
                print("Unable to create loan.")
        elif choice == "10":
            loan_id = int(input("Enter loan ID: "))
            return_date = input("Enter return date: ")

            loan = Loan.search_by_id(loan_id)

            if loan is None:
                print("Loan not found.")
            elif not loan.is_active():
                print("This loan has already been returned.")
            elif loan.return_loan(return_date):
                print("Equipment returned successfully.")
            else:
                print("Unable to return equipment.")
        elif choice == "11":
            while True:
                print("\nSearch")
                print("\n1. Search member by ID")
                print("2. Search member by name")
                print("3. Search member by email")
                print("\n4. Search equipment by ID")
                print("5. Search equipment by name")
                print("6. Search equipment by category")
                print("\n7. Search loan by ID")
                print("8. Search loan by member ID")
                print("9. Search loan by equipment ID")
                print("10. Search loan by checkout date")
                print("11. Search loan by return date")
                print("12. Search active loans")
                print("\n0. Back to main menu")

                search_choice = input("Choose a search option: ")

                if search_choice == "0":
                    break

                elif search_choice == "1":
                    member_id = int(input("Enter member ID: "))
                    member = Member.search_by_id(member_id)

                    if member is None:
                        print("Member not found.")
                    else:
                        print(member)

                elif search_choice == "2":
                    name = input("Enter member name: ")
                    members = Member.search_by_name(name)

                    if not members:
                        print("No members found.")
                    else:
                        for member in members:
                            print(member)

                elif search_choice == "3":
                    email = input("Enter member email: ")
                    members = Member.search_by_email(email)

                    if not members:
                        print("No members found.")
                    else:
                        for member in members:
                            print(member)

                elif search_choice == "4":
                    equipment_id = int(
                        input("Enter equipment ID: ")
                    )
                    equipment = Equipment.search_by_id(equipment_id)

                    if equipment is None:
                        print("Equipment not found.")
                    else:
                        print(equipment)

                elif search_choice == "5":
                    name = input("Enter equipment name: ")
                    equipment_list = Equipment.search_by_name(name)

                    if not equipment_list:
                        print("No equipment found.")
                    else:
                        for equipment in equipment_list:
                            print(equipment)

                elif search_choice == "6":
                    category = input("Enter equipment category: ")
                    equipment_list = Equipment.search_by_category(
                        category
                    )

                    if not equipment_list:
                        print("No equipment found.")
                    else:
                        for equipment in equipment_list:
                            print(equipment)

                elif search_choice == "7":
                    loan_id = int(input("Enter loan ID: "))
                    loan = Loan.search_by_id(loan_id)

                    if loan is None:
                        print("Loan not found.")
                    else:
                        print(loan)

                elif search_choice == "8":
                    member_id = int(input("Enter member ID: "))
                    loans = Loan.search_by_member_id(member_id)

                    if not loans:
                        print("No loans found.")
                    else:
                        for loan in loans:
                            print(loan)

                elif search_choice == "9":
                    equipment_id = int(
                        input("Enter equipment ID: ")
                    )
                    loans = Loan.search_by_equipment_id(
                        equipment_id
                    )

                    if not loans:
                        print("No loans found.")
                    else:
                        for loan in loans:
                            print(loan)

                elif search_choice == "10":
                    checkout_date = input(
                        "Enter checkout date: "
                    )
                    loans = Loan.search_by_checkout_date(
                        checkout_date
                    )

                    if not loans:
                        print("No loans found.")
                    else:
                        for loan in loans:
                            print(loan)

                elif search_choice == "11":
                    return_date = input(
                        "Enter return date: "
                    )
                    loans = Loan.search_by_return_date(
                        return_date
                    )

                    if not loans:
                        print("No loans found.")
                    else:
                        for loan in loans:
                            print(loan)

                elif search_choice == "12":
                    loans = Loan.search_active()

                    if not loans:
                        print("No active loans found.")
                    else:
                        for loan in loans:
                            print(loan)

                else:
                    print("Invalid search option.")
        elif choice == "12":
            while True:
                print("\nReports")
                print("1. Current loans")
                print("2. Member loan history")
                print("3. Equipment loan history")
                print("0. Back to main menu")

                report_choice = input("Choose a report option: ")

                if report_choice == "0":
                    break

                elif report_choice == "1":
                    loans = Loan.current_loans()

                    if not loans:
                        print("No current loans.")
                    else:
                        for loan in loans:
                            print(loan)

                elif report_choice == "2":
                    member_id = int(input("Enter member ID: "))
                    loans = Loan.member_history(member_id)

                    if not loans:
                        print("No loan history found.")
                    else:
                        for loan in loans:
                            print(loan)

                elif report_choice == "3":
                    equipment_id = int(
                        input("Enter equipment ID: ")
                    )
                    loans = Loan.equipment_history(equipment_id)

                    if not loans:
                        print("No loan history found.")
                    else:
                        for loan in loans:
                            print(loan)

                else:
                    print("Invalid report option.")
        else:
            print("Please choose a valid option.")
