from utils import input_error

@input_error
def add_contact(args, contacts):
    # Unpacking the arguments
    name, phone = args
    # Adding a new contact
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    # Unpacking the arguments
    name, phone = args
    # Change the phone number of an existing contact
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def show_phone(args, contacts):
    # Getting a name from arguments
    name = args[0]
    # Search for a contact by name
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    # Forming a row with all contacts
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())