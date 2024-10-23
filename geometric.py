import math
def line_length(dot1, dot2):
    # Extracting coordinates
    x1, y1 = dot1
    x2, y2 = dot2
    
    # Applying the distance formula
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    # Rounding to 2 decimal places
    return round(distance, 2)


# Examples
print(line_length([15, 7], [22, 11]))  # ➞ 8.06
print(line_length([0, 0], [0, 0]))     # ➞ 0
print(line_length([0, 0], [1, 1]))     # ➞ 1.41


def V_DAC(digital_value):
    max_digital_value = 1023  # 10-bit DAC
    reference_voltage = 5.00  # Reference voltage is 5.00V
    
    # Calculate the corresponding analog voltage
    analog_voltage = (digital_value / max_digital_value) * reference_voltage
    
    # Return the voltage rounded to two decimal places
    return round(analog_voltage, 2)

print(V_DAC(0))
print(V_DAC(1023))
print(V_DAC(400))

#Snake Game

def snakefill(n):
    # Total cells on the game screen
    total_cells = n * n
    
    # Initial length of the snake (just the head)
    snake_length = 1
    
    # Counter for how many times the snake eats
    food_eaten = 0
    
    # Loop until the snake runs out of space
    while snake_length <= total_cells:
        food_eaten += 1
        snake_length *= 2  # Snake doubles its length after eating
    
    return food_eaten - 1  # The last doubling exceeds the total cells, so subtract 1

# Example usage:
n = 24
result = snakefill(n)
print(f"The snake can eat {result} times on a {n}x{n} board before running out of space.")
