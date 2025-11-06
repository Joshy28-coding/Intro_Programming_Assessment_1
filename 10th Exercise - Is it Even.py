#10 Exercise: What is the following

def check_even_odd(n):
    """Return whether a number is even or odd."""
    return f"The number {n} is {'even' if n % 2 == 0 else 'odd'}."

def main():
    try:
        num = int(input("Enter a number: "))
        print(check_even_odd(num))
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "_main_":
    main()