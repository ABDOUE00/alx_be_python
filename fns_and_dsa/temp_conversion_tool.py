# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        return celsius
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    try:
        celsius = float(celsius)
        fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
        return fahrenheit
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    try:
        temperature = input("Enter the temperature to convert: ")
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temperature}°F")
        elif unit == 'F':
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temperature}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(e)
