print("Welcome! This program calculates string length.")

while True:
    text = input("\nPlease enter a string (or type 'exit' to quit): ")

    if text.lower() == "exit":
        print("Program exited. Thank you!")
        break

    print("Length of string (using len):", len(text))

    count = 0
    for ch in text:
        count += 1

    print("Length of string (without len):", count)