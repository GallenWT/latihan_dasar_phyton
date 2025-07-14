def decimal_to_binary(number):
    return bin(number)[2:]

def binary_to_decimal(binary_str):
    try:
        return int(binary_str, 2)
    except ValueError:
        return None

def menu():
    print("\n📋 Number Converter:")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    print("3. Exit")

while True:
    menu()
    choice = input("Choose Option (1/2/3): ")

    if choice == "1":
        try:
            number = int(input("Insert whole decimal number: "))
            result = decimal_to_binary(number)
            print(f"🔁 Binary Result: {result}")
        except ValueError:
            print("⚠️ Input must be a whole decimal number.")

    elif choice == "2":
        binary_input = input("Insert binary number (Ex: 1010): ")
        result = binary_to_decimal(binary_input)
        if result is not None:
            print(f"🔁 Decimal result: {result}")
        else:
            print("⚠️  Invalid input. Insert a binary number.")

    elif choice == "3":
        print("👋 Thankyou for using this program.")
        break

    else:
        print("❌ Invalid choice, please try again.")