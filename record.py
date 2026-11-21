from fields import Name, Phone, Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        for number in self.phones:
            if number.value == phone:
                return number
        return None

    def remove_phone(self, phone):
        number = self.find_phone(phone)

        if number:
            self.phones.remove(number)

    def edit_phone(self, old_phone, new_phone):
        number = self.find_phone(old_phone)

        if number:
            i = self.phones.index(number)
            self.phones[i] = Phone(new_phone)
        else:
            raise ValueError("Phone number not found")

    def add_birthday(self, date):
        if self.birthday is not None:
            raise ValueError("Birthday already exists")

        self.birthday = Birthday(date)

    def __str__(self):
        result = (
            f"Contact name: {self.name.value}, "
            f"phones: {'; '.join(p.value for p in self.phones)}"
        )

        if self.birthday is not None:
            result += f", birthday: {self.birthday}"

        return result