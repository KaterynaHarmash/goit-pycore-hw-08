from functools import wraps

from address_book import AddressBook
from record import Record

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except ValueError as e:
            return str(e)

        except KeyError:
            return "Contact not found."

        except IndexError:
            return "Enter required arguments."

    return inner

def parse_input(user_input):
    parts = user_input.split()

    if not parts:
        return "", []

    cmd, *args = parts
    cmd = cmd.lower()

    return cmd, args

@input_error
def add_contact(args, book: AddressBook):
    if len(args) != 2:
        raise ValueError("Usage: add [name] [phone]")

    name, phone = args

    record = book.find(name)

    if record is None:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return "Contact added."

    record.add_phone(phone)
    return "Contact updated."


@input_error
def change_contact(args, book: AddressBook):
    if len(args) != 3:
        raise ValueError(
            "Usage: change [name] [old phone] [new phone]"
        )

    name, old_phone, new_phone = args

    record = book.find(name)

    if record is None:
        raise KeyError

    record.edit_phone(old_phone, new_phone)

    return "Contact updated."


@input_error
def show_phone(args, book: AddressBook):
    if len(args) != 1:
        raise ValueError("Usage: phone [name]")

    name = args[0]

    record = book.find(name)

    if record is None:
        raise KeyError

    if not record.phones:
        return "No phone numbers found."

    return "; ".join(str(phone) for phone in record.phones)


@input_error
def show_all(book: AddressBook):
    if book:
        return "\n".join(
            str(record) for record in book.values()
        )

    return "No contacts found."


@input_error
def add_birthday(args, book: AddressBook):
    if len(args) != 2:
        raise ValueError(
            "Usage: add-birthday [name] [DD.MM.YYYY]"
        )

    name, date = args

    record = book.find(name)

    if record is None:
        raise KeyError

    record.add_birthday(date)

    return "Birthday added."


@input_error
def show_birthday(args, book: AddressBook):
    if len(args) != 1:
        raise ValueError("Usage: show-birthday [name]")

    name = args[0]

    record = book.find(name)

    if record is None:
        raise KeyError

    if record.birthday is None:
        return f"{name} has no birthday added."

    return str(record.birthday)


@input_error
def birthdays(args, book: AddressBook):
    if args:
        raise ValueError("Usage: birthdays")

    upcoming = book.get_upcoming_birthdays()

    if not upcoming:
        return "No upcoming birthdays."

    return "\n".join(
        f"{item['name']}: {item['congratulation_date']}"
        for item in upcoming
    )

def main():
    book = AddressBook()

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
