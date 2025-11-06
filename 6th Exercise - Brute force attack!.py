#6 Exercise: Brute Force Attack!

Correct_password = "JesusLovesYou"
max_attempts = 5
attempts = 0

print("\nHold it right there! to proceed further you must enter the correct password!")
while attempts < max_attempts:
    hulaanmo = input("\n---\n\nEnter the password: ").strip()
    attempts += 1
    if hulaanmo == Correct_password:
        print("Correct Password detected - Access granted!")
        break
    else:
        uhohguessagain = max_attempts - attempts
        if uhohguessagain > 0:
            print(f"Tick, tick, tick! {uhohguessagain} attempts remaining, try again!")
        else:
            print("BOOM! No more attempts remaining!")
            print("It does not matter who you are, Christ made sure you are a miracle from the day you we're formed.")