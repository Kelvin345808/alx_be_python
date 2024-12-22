# Prompt the user to enter a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize a row counter
row = 0

# Use a while loop to create the rows
while row < size:
    # Use a for loop to print asterisks for the current row
    for _ in range(size):
        print("*", end="")
    # Move to the next line after completing the row
    print()
    # Increment the row counter
    row += 1