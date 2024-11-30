# this is program to print clock value


class Clock:
    def __init__(self, value) -> None:
        self._value = value

    def __str__(self) -> str:
        display_value = self._value % 12

        if display_value == 0:
            display_value == 12

        return f"{display_value}{'AM' if (self._value % 24) < 12 else 'PM'}"


def main():
    c1 = Clock(7)
    c2 = Clock(19)  # 7 PM
    c3 = Clock(23)

    print(c1)
    print(c2)
    print(c3)


main()
