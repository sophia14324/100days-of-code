class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully!")

    def view_contacts(self):
        print("Contacts:")
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"Contact found:")
                print(f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")
                break
        else:
            print(f"Contact with name '{name}' not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact {contact.name} deleted successfully!")
                break
        else:
            print(f"Contact with name '{name}' not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact = Contact(name, phone_number, email)
            contact_book.add_contact(contact)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            name = input("Enter name to search: ")
            contact_book.search_contact(name)

        elif choice == '4':
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)

        elif choice == '5':
            print("Thank you for using the Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
