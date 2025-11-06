# Exercise 3: Biography 

def get_full_name():
    full = input("\nEnter your first and last name: ").strip()
    if not full:
        return "", ""
    parts = full.split(maxsplit=1)
    first = parts[0]
    last = parts[1] if len(parts) > 1 else ""
    return first, last

def get_hometown():
    while True:
        x = input("\nEnter your hometown: ").strip()
        livingonthemoon = x.lower()
        if "moon" in livingonthemoon:
            print("You live on the moon!? Please enter a real hometown.")
            continue
        return x

def age_str():
    while True:
        s = input("\nEnter your age (numbers only): ").strip()
        try:
            age = int(s)
            if age < 0:
                print(age, "Years old? seriously? Try again")
                continue
            if age > 150:
                print("There is no way you are that old")
                continue
            return age
        except ValueError:
            print("That's not a valid number. Please use digits, e.g. 18.")

first_name, last_name = get_full_name()        
hometown = get_hometown()
age = age_str()

if "muniba" in first_name.lower():
    print("\n---\n\nMiss Muniba! You are so cool and smart! Thank you for being our Creative Computing Level 4 instructor!")
elif first_name:
    print(f"\n--\n\nWow your name is {first_name}. Nice meeting you! You are really cool!")

print(f"\nYou live in {hometown}! Pretty cool — you must be rich or something..")
print(f"\nYou are {age} years old! You are very young! (What Filipinos love to say despite whatever age.)")

biography = {
    "FirstName": first_name,
    "LastName": last_name,
    "FullName": (first_name + " " + last_name).strip(),
    "Hometown": hometown,
    "Age": age
}

print(biography)