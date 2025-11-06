#Exercise 8: Search for Sam
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave", "Sam"]
target = input("\n---\n\nEnter the name to search for: ").strip()

indices = [i for i, n in enumerate(names) if n == target]

if indices:
    print(f"Found {target} at indices: {indices}")
else:
    print(f"{target} not found in the list.")
