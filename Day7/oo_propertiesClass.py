# Program for property class


class Person:
    def __init__(self, age) -> None:
        self._age = age  # Initializes the age

    def get_age(self):
        return self.age  # Getter method for age

    def __str__(self) -> str:
        return f"Preson of age {self._age}"

    def set_age(self, age):
        # Setter method to validate age
        if age < 0 or age > 100:
            raise ValueError(f"Age {age} out of range")
        self._age = age  # Set the age

    # Use the property decorator to manage getting and setting age
    age = property(fget=get_age, fset=set_age)


def main():
    person1 = Person(40)

    # The print statement will use the default object representation
    print(person1)  # This prints the memory address, not the age


main()
