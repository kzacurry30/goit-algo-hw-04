def add_contact(contacts, name, phone):
    contacts[name] = phone
    print("Contact added.")

def change_contact(contacts, name, phone):
    if name in contacts:
        contacts[name] = phone
        print("Contact updated.")
    else:
        print("Error: Contact not found.")

def show_phone(contacts, name):
    if name in contacts:
        print(contacts[name])
    else:
        print("Error: Contact not found.")

def show_all(contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")

def parse_input(user_input):
    parts = user_input.strip().split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args

def main():
    contacts = {}
    print("Welcome to the assistant bot. Type 'help' to see the list of commands.")

    while True:
        user_input = input("> ")
        command, args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")
        elif command == "help":
            print("Available commands:")
            print("  hello")
            print("  add [name] [phone]")
            print("  change [name] [new phone]")
            print("  phone [name]")
            print("  all")
            print("  exit or close")
        elif command == "add":
            if len(args) != 2:
                print("Invalid command. Usage: add [name] [phone]")
            else:
                add_contact(contacts, args[0], args[1])
        elif command == "change":
            if len(args) != 2:
                print("Invalid command. Usage: change [name] [new phone]")
            else:
                change_contact(contacts, args[0], args[1])
        elif command == "phone":
            if len(args) != 1:
                print("Invalid command. Usage: phone [name]")
            else:
                show_phone(contacts, args[0])
        elif command == "all":
            show_all(contacts)
        elif command in ["exit", "close"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Type 'help' to see the list of commands.")

if __name__ == "__main__":
    main()
