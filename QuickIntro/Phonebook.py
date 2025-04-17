phonebook = {}


def add_contact(name, number):
    phonebook[name] = number
    print(f"Contact `{name}` added with number {number}")


def remove_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"Contact `{name}` removed")
    else:
        print(f"Contact `{name}` not found")


def display_contacts():
    print("Phonebook:")
    for name, number in phonebook.items():
        print(f"{name}: {number}")


add_contact("Alice", "123-456-7890")
add_contact("Bob", "987-654-3210")
add_contact("Charlie", "555-555-5555")


display_contacts()


remove_contact("Bob")


display_contacts()


print(phonebook)
