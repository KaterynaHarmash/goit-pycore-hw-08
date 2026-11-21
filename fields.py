from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        value = value.strip()

        if not value:
            raise ValueError("Name cannot be empty")

        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        value = value.strip()

        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone must contain exactly 10 digits")

        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            value = value.strip()
            date = datetime.strptime(value, "%d.%m.%Y")

            if date.strftime("%d.%m.%Y") != value:
                raise ValueError

            super().__init__(date)

        except ValueError:
            raise ValueError(
                "Invalid date format. Use DD.MM.YYYY"
            )

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")