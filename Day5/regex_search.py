# Program for regex search


import re


def main():

    text = """

      one,
      two,
      three

      """

    result = re.search(r"t.*e", text)

    if result is None:
        print("No match")

    else:
        print(f"{result.group()}")


main()
