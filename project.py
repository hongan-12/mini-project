import random
# ==============================
# GUESS THE NUMBER GAME
# ==============================

print("=" * 50)
print(" GUESS THE NUMBER")
print("=" * 50)
print("Welcome to Guess The Number!")
print("Try to find the secret number!")
print("You have a maximum of 7 attempts.")

# Main game loop
while True:

    # Choose difficulty
    print("\n========== DIFFICULTY ==========")
    print("1. Easy   (1 - 50)")
    print("2. Medium (1 - 100)")
    print("3. Hard   (1 - 500)")

    difficulty = input("\nChoose your difficulty (1/2/3): ")

    if difficulty == "1":
        maximum = 50
        level_name = "Easy"

    elif difficulty == "2":
        maximum = 100
        level_name = "Medium"

    elif difficulty == "3":
        maximum = 500
        level_name = "Hard"
    else:
        print("Invalid choice! Please try again.")
        continue
    # Generate random secret number

    secret_number = random.randint(1, maximum)

    # Game settings
    max_attempts = 7
    attempts = 0
    guessed = False
    print("\n" + "=" * 50)
    print(f"Difficulty: {level_name}")
    print(f"The computer has chosen a number from 1 to {maximum}.")
    print("You have 7 attempts. Good luck!")
    print("=" * 50)

    # Guessing loop
    while attempts < max_attempts:
        try:
            guess = int(input(
                f"\nAttempt [{attempts + 1}/7] - Enter your guess: "
            ))
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            continue

        # Check input range
        if guess < 1 or guess > maximum:
            print(f"Please enter a number between 1 and {maximum}.")
            continue

        # Count valid attempts
        attempts += 1

        # Compare the guess with the secret number
        if guess < secret_number:
            print("🔼 HINT: The secret number is HIGHER!")
        elif guess > secret_number:
            print("🔽 HINT: The secret number is LOWER!")
        else:
            guessed = True
            print("\n CONGRATULATIONS!")
            print(f"You guessed the correct number: {secret_number}!")
            break

    # Calculate score and rank
    if guessed:
        score = (8 - attempts) * 15

        if attempts <= 2:
            rank = "LEGENDARY GUESSER"

        elif attempts <= 4:
            rank = "EXPERT"

        else:
            rank = "BEGINNER"
        print("\n========== GAME RESULTS ==========")
        print(f"Difficulty: {level_name}")
        print(f"Attempts used: {attempts}/7")
        print(f"Your score: {score} points")
        print(f"Your rank: {rank}")
        print("==================================")
    else:
        print("\n GAME OVER!")
        print("You have used all 7 attempts.")
        print(f"The secret number was: {secret_number}")
        print("Your score: 0 points")
        
    # Ask to play again
    print("\n==================================")
    play_again = input("Would you like to play again? (y/n): ")
    if play_again.lower() != "y":
        print("\nThank you for playing Guess The Number!")
        print("See you next time! ")
        break
