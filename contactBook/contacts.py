import re
import sqlite3
from enum import Enum
from dataclasses import dataclass


class Choices(Enum):
    ADD = 1
    FIND = 2
    UPDATE = 3
    DELETE = 4
    LIST = 5
    EXIT = 6


@dataclass
class IContact:
    name: str
    address: str
    phone: str
    email: str


class ContactBook:
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY,
                name TEXT,
                address TEXT,
                phone TEXT,
                email TEXT
            )
        """
        )
        self.conn.commit()

    @property
    def name(self):
        while True:
            name = input("Enter name: ").title()
            name_regex = re.compile(r"^[A-Z][a-z]*(?: [A-Z][a-z]*)*$")
            if not name_regex.match(name):
                print("Invalid name")
                self.name
            break
        return name

    @property
    def address(self):
        while True:
            address = input("Enter address: ")
            address_regex = re.compile(r"[\w\d\s\S]*")
            if not address_regex.match(address):
                print("Invalid address")
                self.address
            break
        return address

    @property
    def phone(self):
        while True:
            phone = input("Enter phone number: ")
            phone_regex = re.compile(r"[+\d].*")
            if not phone_regex.match(phone):
                print("Invalid phone number")
                self.phone
            break
        return phone

    @property
    def email(self):
        while True:
            email = input("Enter email address: ")
            email_regex = re.compile(
                r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
            )
            if not email_regex.match(email):
                print("Invalid email address")
                self.email
            break
        return email

    # Note: It looks like repetition below but it's absolutely not.
    # The update parameters have different regular expresiions,
    # allowing for blank values for users that wish to leave retain the previous value

    @property
    def update_name(self):
        while True:
            name = input("Enter new name (leave blank to keep existing): ").title()
            name_regex = re.compile(r"^(\s*|\b\w+\b(\s+\w+)*\b)$")
            if not name_regex.match(name):
                print("Invalid name! Please try again...")
                self.update_name
            break
        return name

    @property
    def update_address(self):
        while True:
            address = input("Enter new address (leave blank to keep existing): ")
            address_regex = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9\s]*$|^$")
            if not address_regex.match(address):
                print("Invalid address! Please try again...")
                self.update_address
            break
        return address

    @property
    def update_email(self):
        while True:
            email = input("Enter new email (leave blank to keep existing): ")
            email_regex = re.compile(
                r"^\s*([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})?\s*$"
            )
            if not email_regex.match(email):
                print("Invalid email address! Please try again...")
                self.update_email
            break
        return email

    @property
    def update_phone(self):
        while True:
            phone = input("Enter new phone number (leave blank to keep existing): ")
            phone_regex = re.compile(r"^(\+|\d)?([\s-]*\d[\s-]*)*$")
            if not phone_regex.match(phone):
                print("Invalid phone number! Please try again...")
                self.update_phone
            break
        return phone

    def add_contact(self, contact: IContact) -> None:
        self.cursor.execute(
            """
            INSERT INTO contacts (name, address, phone, email)
            VALUES (?, ?, ?, ?)
        """,
            (contact.name, contact.address, contact.phone, contact.email),
        )
        self.conn.commit()
        print()
        print("Contact added successfully!")

    def find_contact(self, id: int) -> tuple[int, str, str, str, str]:
        self.cursor.execute(
            """
            SELECT id, name, address, phone, email
            FROM contacts
            WHERE id = ?
        """,
            (id,),
        )
        result = self.cursor.fetchone()
        return result

    def update_contact(self, id: int, contact: IContact) -> None:
        self.cursor.execute(
            """
            UPDATE contacts
            SET name=?, address=?, phone=?, email=?
            WHERE id=?
        """,
            (contact.name, contact.address, contact.phone, contact.email, id),
        )
        self.conn.commit()

    def delete_contact(self, id: int) -> None:
        self.cursor.execute("SELECT * FROM contacts WHERE id=?", (id,))
        if self.cursor.fetchone():   
            self.cursor.execute(
                """
                DELETE FROM contacts
                WHERE id=?
            """,
                (id,),
            )
            self.conn.commit()
            print()
            print(f"Contact with ID: {id} has been deleted successfully!")
        # result = self.cursor.fetchone()
        else:
            print()
            print(f"Contact with ID: {id} does not exist!")
            

    def list_contacts(self) -> list[tuple[int, str, str, str, str]]:
        self.cursor.execute(
            """
            SELECT id, name, address, phone, email
            FROM contacts
        """
        )
        result = self.cursor.fetchall()
        return result

    @classmethod
    def get_queryset(cls, qs):
        print()
        print("Id:", qs[0])
        print("Name:", qs[1])
        print("Address:", qs[2])
        print("Phone:", qs[3])
        print("Email:", qs[4])

    def user_choices(self):
        while True:
            print("**********************")
            print("     Contact Book     ")
            print("**********************\n")
            print("1. Add Contact")
            print("2. Find Contact")
            print("3. Update Contact")
            print("4. Delete Contact")
            print("5. List Contacts")
            print("6. Exit\n")

            try:
                case = int(input("Enter your choice: "))
                if case == Choices.ADD.value:
                    return "1"
                elif case == Choices.FIND.value:
                    return "2"
                elif case == Choices.UPDATE.value:
                    return "3"
                elif case == Choices.DELETE.value:
                    return "4"
                elif case == Choices.LIST.value:
                    return "5"
                elif case == Choices.EXIT.value:
                    return "6"
                else:
                    return "Invalid Response"
            except ValueError:
                print("Invalid Response! Please try again...")
                print()
                self.user_choices()
            break


def main():
    app = ContactBook("contact.sqlite3")
    while True:
        choice = app.user_choices()
        if choice == "1":
            name = app.name
            address = app.address
            phone = app.phone
            email = app.email
            contact = IContact(name, address, phone, email)
            app.add_contact(contact)
            print()
        elif choice == "2":
            id = input("Enter Contact ID: ")
            result = app.find_contact(id)
            if result:
                print()
                print("1 contact found!")
                app.get_queryset(result)
            else:
                print("Contact not found!")
            print()
        elif choice == "3":
            id = int(input("Enter contact id: "))
            print()
            name = app.update_name
            address = app.update_address
            phone = app.update_phone
            email = app.update_email
            print()
            old_contact = app.find_contact(id)
            if not old_contact:
                print("Contact not found.")
            else:
                new_contact = IContact(
                    name if name else old_contact[1],
                    address if address else old_contact[2],
                    phone if phone else old_contact[3],
                    email if email else old_contact[4],
                )
                app.update_contact(id, new_contact)
                print("Contact updated successfully.")
                print()
        elif choice == "4":
            id = input("Enter the id of the contact to delete: ")
            app.delete_contact(id)
            print()
        elif choice == "5":
            query = app.list_contacts()
            if query:
                print("Contacts:")
                for qs in query:
                    app.get_queryset(qs)
            else:
                print("No contacts found!")
            print()
        elif choice == "6":
            break
        else:
            print("Invalid Request! Please try again.\n")

    app.conn.close()


if __name__ == "__main__":
    main()
