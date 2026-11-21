from collections import UserDict
from datetime import datetime, timedelta

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        self.data.pop(name, None)

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        end_of_week = today + timedelta(days=7)

        upcoming_birthdays = []

        for record in self.values():

            if record.birthday is None:
                continue

            birthday_date = record.birthday.value.date()

            # Create birthday date for the current year.
            # February 29 becomes February 28 in non-leap years.
            try:
                birthday_this_year = birthday_date.replace(
                    year=today.year
                )
            except ValueError:
                birthday_this_year = birthday_date.replace(
                    year=today.year,
                    day=28
                )

            # If the birthday has already passed,
            # consider next year.
            if birthday_this_year < today:
                try:
                    birthday_this_year = birthday_date.replace(
                        year=today.year + 1
                    )
                except ValueError:
                    birthday_this_year = birthday_date.replace(
                        year=today.year + 1,
                        day=28
                    )

            # Check whether birthday falls within the next 7 days.
            if today <= birthday_this_year <= end_of_week:

                congratulation_date = birthday_this_year

                # Move weekend birthdays to the following Monday.
                if birthday_this_year.weekday() == 5:
                    congratulation_date += timedelta(days=2)

                elif birthday_this_year.weekday() == 6:
                    congratulation_date += timedelta(days=1)

                upcoming_birthdays.append({
                    "name": record.name.value,
                    "congratulation_date":
                        congratulation_date.strftime("%Y.%m.%d")
                })

        return upcoming_birthdays