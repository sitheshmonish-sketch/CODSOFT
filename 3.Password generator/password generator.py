import random
import string

print("===== PASSWORD GENERATOR =====")

# Get password length from the user
length = int(input("Enter the desired password length: "))

# Character set (letters, digits, and special characters)
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = "".join(random.choice(characters) for i in range(length))

# Display the generated password
print("\nGenerated Password:")
print(password)
