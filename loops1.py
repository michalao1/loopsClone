
#!/usr/bin/python
# what is this doing?
# This code uses nested loops to print the values of x and y
for x in range(0, 8):
    for y in range(0, 16):
        if x < 4 and y < 8:
            print(f"({x}, {y}) is in the first quadrant.")  # Prints a message if the coordinates are in the first quadrant
        elif x >= 4 and y < 8:
            print(f"({x}, {y}) is in the second quadrant.")  # Prints a message if the coordinates are in the second quadrant
        elif x >= 4 and y >= 8:
            print(f"({x}, {y}) is in the third quadrant.")  # Prints a message if the coordinates are in the third quadrant
        else:
            print(f"({x}, {y}) is in the fourth quadrant.")  # Prints a message if the coordinates are in the fourth quadrant
      

  
