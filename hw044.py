def parse_input(user_input):
    """
    Parse user input into command and arguments.
    """
    parts = user_input.strip().split()
    command = parts[0].lower() if parts else ''
    args = parts[1:] if len(parts) > 1 else []
    return command, args

def add_contact(contacts, name, phone):
    """
    Add a new contact to the contacts dictionary.
    """
    contacts[name] = phone
    return "Contact added."

def change_contact(contacts, name, phone):
    """
    Change the phone number of an existing contact.
    """
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Error: contact not found."

def show_phone(contacts, name):
    """
    Show the phone number of a contact.
    """
    if name in contacts:
        return contacts[name]
    else:
        return "Error: contact not found."

def show_all(contacts):
    """
    Show all contacts with their phone numbers.
    """
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."

def main():
    contacts = {}
    while True:
        user_input = input("> ")
        command, args = parse_input(user_input)
        
        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) == 2:
                name, phone = args
                print(add_contact(contacts, name, phone))
            else:
                print("Invalid command. Usage: add [name] [phone]")
        elif command == "change":
            if len(args) == 2:
                name, phone = args
                print(change_contact(contacts, name, phone))
            else:
                print("Invalid command. Usage: change [name] [phone]")
        elif command == "phone":
            if len(args) == 1:
                name = args[0]
                print(show_phone(contacts, name))
            else:
                print("Invalid command. Usage: phone [name]")
        elif command == "all":
            print(show_all(contacts))
        elif command in ("close", "exit"):
            print("Good bye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()