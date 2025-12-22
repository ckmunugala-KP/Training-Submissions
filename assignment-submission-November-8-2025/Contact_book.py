
contacts = []

def add_contact(name, phone, email):
    """Add a new contact as a tuple"""
    contact = (name, phone, email)
    contacts.append(contact)
    print(f"\n✅ Contact '{name}' added successfully!")

def view_contacts():
    """Display all contacts"""
    if not contacts:
        print("\nNo contacts found.")
        return
    print("\n📘 Contact List:")
    for idx, (name, phone, email) in enumerate(contacts, start=1):
        print(f"{idx}. Name: {name}, Phone: {phone}, Email: {email}")

def search_contact(name):
    """Search for a contact by name"""
    for contact in contacts:
        if contact[0].lower() == name.lower():
            print(f"\n🔍 Found Contact: Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")
            return
    print(f"\n❌ No contact found with name '{name}'")

def delete_contact(name):
    """Delete a contact by name"""
    global contacts
    contacts = [c for c in contacts if c[0].lower() != name.lower()]
    print(f"\n🗑️ Contact '{name}' deleted (if existed).")

while True:
    print("\n==== Contact Book Menu ====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        add_contact(name, phone, email)
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        name = input("Enter name to search: ")
        search_contact(name)
    elif choice == '4':
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == '5':
        print("\n👋 Exiting Contact Book. Goodbye!")
        break
    else:
        print("\n❗ Invalid choice. Please enter a number between 1 and 5.")
