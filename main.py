#!/usr/bin/python3
"""The main interface of the system."""

from database import create_tables, add_member


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

            member_id = add_member(name, email)

            print("Member registered successfully!")
            print("Member ID: ", member_id)

if __name__ == "__main__":
    main()
