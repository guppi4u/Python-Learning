# Program for converting miles into feet or vice versa


import sys

# this is return feet converted to miles


def feetToMiles(feet):
    return feet * 1.89E-4


def main():
    while True:  # Start an infinite loop
        feet = input("Enter distance in feet (or type 'quit' to exit): ")

        if feet.lower() == "quit":  # Check if the user wants to exit
            break  # Exit the loop

        try:
            # Convert input to an integer and calculate miles
            miles = feetToMiles(int(feet))
            print(f"{feet} is equivalent to {
                  miles:.3f} miles.")  # Print the result

        except ValueError:  # Catch specific exceptions
            print("Invalid input. Please enter a number or 'quit'.")


if __name__ == "__main__":
    main()  # Call the main function
