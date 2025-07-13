
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "⚠️ Error, can't divide by zero!"
def menu():
    print("\n📋 Operation Menu:")
    print("1. Addition       (+)")
    print("2. Subtraction    (-)")
    print("3. Multiplication (*)")
    print("4. Division       (/)")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == "5":
        print("👋 Thankyou for using this calculator!")
        break
    try:
        if choice in ["1", "2", "3", "4"]:
            first_num = float(input("Insert first number: "))
            second_num = float(input("Insert second number: "))
    except ValueError:
        print("⚠️ Input must be a number.")
        continue

    match choice:
        case "1":
            result = addition(first_num,second_num)
            operation = '+'
        case "2":
            result = subtraction(first_num,second_num)
            operation = '-'
        case "3":
            result = multiplication(first_num,second_num)
            operation = '*'
        case "4":
            result = division(first_num,second_num)
            operation = '/'
        case _:
            print("Choose a valid choice.")

    print(f"🧮 Result: {first_num} {operation} {second_num} = {result}")