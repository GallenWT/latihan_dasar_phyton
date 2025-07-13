import random

randomNumber = random.randint(1,100)
attempt = 1
max_attempts = 7

print("🎯 Welcome to the Guess the Number Game!")
print("I've picked a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it.\n")

while attempt <= max_attempts:
    try:
        guessNumber = int(input(f"Attempt {attempt}/{max_attempts} - Enter your guess: "))
    except ValueError:
        print("⚠️ Invalid input! Please enter a valid number.\n")
        continue

    if guessNumber == randomNumber:
        print(f"🎉 Correct! You guessed the number in {attempt} attempt(s).")
        break
    elif guessNumber > randomNumber:
        print("⬆️ Too high! Try a smaller number.\n")
    elif guessNumber < randomNumber:
        print("⬇️ Too low! Try a bigger number.\n")

    attempt += 1

    if attempt > max_attempts:
        print(f"❌ Game Over! The correct number was {randomNumber}.\n")
        break