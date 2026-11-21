# Personal Assistant — CLI Contact Book

A command-line personal assistant for managing contacts, phone numbers, and birthdays.

The application is built with Python using object-oriented programming (OOP) principles. It provides a simple command-line interface for managing an address book, tracking upcoming birthdays, and preserving contact data between application runs.

## Features

- Add new contacts.
- Add multiple phone numbers to a contact.
- Edit existing phone numbers.
- Find contacts and display their phone numbers.
- Display all contacts.
- Add and view birthdays.
- Display upcoming birthdays within the next 7 days.
- Move weekend birthday greetings to the following Monday.
- Validate user input and handle errors.
- Save and restore contact data using Python pickle serialization.

## Project Structure

```text
.
├── assistant.py       # Command-line interface and command handlers
├── fields.py          # Field, Name, Phone and Birthday classes
├── record.py          # Record class for contact management
├── address_book.py    # AddressBook class and birthday calculations
├── storage.py         # Saving and loading address book data
├── addressbook.pickle # Serialized address book data (generated at runtime)
└── README.md
```

## Requirements

- Python 3.10 or later
- No external dependencies required (Python standard library only)

## Available Commands

| Command | Description | Example |
|---|---|---|
| `hello` | Display a welcome message | `hello` |
| `add` | Add a contact or another phone number | `add John 1234567890` |
| `change` | Change an existing phone number | `change John 1234567890 0987654321` |
| `phone` | Display a contact's phone numbers | `phone John` |
| `all` | Display all contacts | `all` |
| `add-birthday` | Add a birthday to a contact | `add-birthday John 19.11.1993` |
| `show-birthday` | Display a contact's birthday | `show-birthday John` |
| `birthdays` | Display upcoming birthdays | `birthdays` |
| `close` / `exit` | Save data and exit the application | `exit` |

## Data Validation

The application validates user input:

- **Name:** cannot be empty.
- **Phone:** must contain exactly 10 digits.
- **Birthday:** must be a valid date in `DD.MM.YYYY` format.
- **Contact lookup:** operations requiring an existing contact return an error if the contact is not found.
- **Birthday uniqueness:** a contact cannot have more than one birthday assigned.

Input errors are handled using the `input_error` decorator.

## Object-Oriented Design

The application is divided into modules according to their responsibilities.

### `fields.py`

Contains the base `Field` class and its specialized subclasses:

- `Name` — stores and validates contact names.
- `Phone` — stores and validates phone numbers.
- `Birthday` — stores and validates dates of birth.

### `record.py`

Contains the `Record` class, representing an individual contact.

Main methods:

- `add_phone()` — adds a phone number.
- `find_phone()` — searches for a phone number.
- `edit_phone()` — updates a phone number.
- `remove_phone()` — removes a phone number.
- `add_birthday()` — assigns a birthday.

### `address_book.py`

Contains the `AddressBook` class, based on Python's `collections.UserDict`.

Main methods:

- `add_record()` — adds a contact.
- `find()` — finds a contact by name.
- `delete()` — removes a contact.
- `get_upcoming_birthdays()` — retrieves upcoming birthdays.

### `storage.py`

Handles persistent storage of the address book using Python's `pickle` module.

Main functions:

- `save_data()` — serializes the address book and saves it to `addressbook.pickle`.
- `load_data()` — deserializes and restores the address book when the application starts.
- If the storage file does not exist, `load_data()` returns a new, empty `AddressBook`.

The application automatically loads saved contact data on startup and saves it when the user exits using the `close` or `exit` command.

## Data Persistence

Contact data is stored between application runs using Python pickle serialization.

The persistence workflow:

1. When the application starts, it attempts to load the address book from `addressbook.pickle`.
2. If the file does not exist, a new empty address book is created.
3. During the session, contacts and their information are managed in memory.
4. When the user enters `close` or `exit`, the current address book is serialized and saved to the file.
5. On the next launch, the saved data is restored automatically.

The `addressbook.pickle` file is generated automatically and does not need to be created manually.

## Upcoming Birthdays

The `birthdays` command returns contacts whose birthdays fall within the next 7 days.

Additional rules:

- Birthdays falling on Saturday are moved to Monday.
- Birthdays falling on Sunday are moved to Monday.
- February 29 birthdays are handled in non-leap years by using February 28.

## Limitations

- The application is designed for command-line interaction.
- Phone numbers are stored as strings and validated as 10-digit numeric values.
- Data is saved when the application is closed using the `close` or `exit` command. Unexpected termination may prevent the latest changes from being saved.

## Learning Objectives

This project demonstrates practical use of:

- Object-oriented programming in Python.
- Classes, inheritance and encapsulation.
- Custom data types and validation.
- Python collections and `UserDict`.
- Decorators and exception handling.
- Modular application structure and imports.
- Date and time manipulation with `datetime`.
- Data serialization and deserialization with `pickle`.
- Persistent storage of Python objects.
