# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Use a while loop to draw the pattern
row = 1
while row <= size:
    # Use a for loop to print asterisks (*) in each row
    for col in range(size):
        print("*", end="")
    # Move to the next line after each row
    print()
    row += 1
