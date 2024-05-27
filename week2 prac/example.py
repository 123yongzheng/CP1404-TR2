import random


def print_smiley_faces(low, high):
    if high <= low:
        print("Error: The high number must be greater than the low number.")
        return

    n = random.randint(low, high)
    print("Printing", n, "smiley faces:")
    print("😊" * n)


def main():
    low = int(input("Enter a low number: "))
    high = int(input("Enter a high number: "))

    print_smiley_faces(low, high)


if __name__ == "__main__":
    main()
