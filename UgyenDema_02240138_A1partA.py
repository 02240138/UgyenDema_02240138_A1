def is_prime(n):
    # Check if a number is prime.
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_sum(start, end):
    # Calculate the sum of prime numbers in a given range.
    return sum(n for n in range(start, end + 1) if is_prime(n))

def convert_length(value, direction):
    # Convert length between meters and feet.
    if direction == 'M':
        return round(value * 3.28084, 2)  # Meters to feet
    elif direction == 'F':
        return round(value / 3.28084, 2)  # Feet to meters
    else:
        return "Invalid direction"

def count_consonants(text):
    # Count the number of consonants in a given string.
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char.isalpha() and char not in vowels)

def find_min_max(numbers):
    # Find the smallest and largest numbers in a given list.
    return min(numbers), max(numbers)

def is_palindrome(text):
    # Check if a given string is a palindrome (ignoring case and spaces).
    cleaned_text = ''.join(text.lower().split())
    return cleaned_text == cleaned_text[::-1]

def main():
    while True:
        print("\nSelect a function (1-5):")
        print("1. Calculate the sum of prime numbers")
        print("2. Convert length units")
        print("3. Count consonants in a string")
        print("4. Find min and max in a list of numbers")
        print("5. Check if a string is a palindrome")
        print("6. Exit")

        choice = input(" your choice: ")

        if choice == '1':
            start = int(input("Enter starting of range: "))
            end = int(input("Enter ending of range: "))
            print(f"Sum of prime numbers: {prime_sum(start, end)}") # type: ignore

        elif choice == '2':
            value = float(input("Enter numeric value: "))
            direction = input("Enter direction ('M' for meters to feet, 'F' for feet to meters): ").upper()
            print(f"Converted length: {convert_length(value, direction)}")

        elif choice == '3':
            text = input("Enter a text string: ")
            print(f"Number of consonants: {count_consonants(text)}")

        elif choice == '4':
            numbers = list(map(int, input("Enter numbers separated by space: ").split()))
            smallest, largest = find_min_max(numbers)
            print(f"Smallest: {smallest}, Largest: {largest}")

        elif choice == '5':
            text = input("Enter a text string: ")
            print(f"Palindrome: {is_palindrome(text)}")

        elif choice == '6':
            print("Exiting.")
            break
        else:
            print("Invalid! Please select a valid option.")

if __name__ == "__main__":
    main()
    