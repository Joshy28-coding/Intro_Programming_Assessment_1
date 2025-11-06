#5 Exercise: Days in a month

def daysinamonth():
    month_days = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    m = input("\nEnter month number (1-12): ").strip()
    try:
        month = int(m)
    except ValueError:
        print("There are 13+ months?! \nInvalid Input - Please enter a number of a month between 1 and 12.\n")
        return 
    
    if 1 <= month <= 12:
        if month == 2:
            ans = input("Is it a leap year? (yes/no): ").strip().lower()
            if ans in ("yes", "y"):
                print("February has 29 days.")
            else:
                print("February has 28 days.")
        else:
            print(f"Month {month} has {month_days[month]} days.")
    else:
        print("Invalid month number. Please enter 1-12.")

if __name__ == "__main__":
    daysinamonth()