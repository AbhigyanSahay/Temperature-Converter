# This program will convert your Celsius value to Fahrenheit value

print("Hello! Welcome to the Temperature Converter program.")

# A for Celsius 
# B for Fahrenheit

print("\nEnter 'a' for celsius to fahrenheit or 'b' for fahrenheit to celsius.")
print("Enter your choice:")

choice1 = input()
choice1 = choice1.lower()

print("\nEnter the temperature that is to be converted:")
choice2 = input()

# Degree Fahrenheit = (Degree Celsius * 9/5) + 32
# Degree Celsius = (Degree Fahrenheit - 32) * 5/9

if choice1 == "a":
    c = int(choice2)

    f = (c * (9/5)) + 32
    print(f"The temperature of {c} degree Celsius is {f} degree Fahrenheit.")

elif choice1 == "b":
    f = int(choice2)

    c = (f - 32) * (5/9)
    print(f"The temperature of {f} degree Fahrenheit is {c} degree Celsius.")


else:
    print("Invalid Option!")
