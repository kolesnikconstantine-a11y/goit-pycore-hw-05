def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            "Enter the argument for the command"
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command"
    return inner

@input_error
def change_contact(args, contacts):
    name, phone = args
    for key in contacts:
        if key == name:
            contacts[key] = phone
            return "Contact updated."
    else:
        return "No such contact"

@input_error
def show_phone(args, contacts):
    name = args[0]
    for key, value in contacts.items():
        if key == name:
            return value
    else:
        return "No such contact"
    
@input_error
def show_all(contacts):
     for key ,value in contacts.items():
         print(key , value)
        
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            show_all(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
