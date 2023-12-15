def temperature_converter():
  """
  Converts between Celsius and Fahrenheit.
  """
  while True:
    try:
      # Get user input
      value = float(input("Enter the temperature: "))
      source_unit = input("Enter the source unit (C or F): ").lower()
      target_unit = input("Enter the target unit (C or F): ").lower()

      # Validate units
      if source_unit not in ("c", "f") or target_unit not in ("c", "f"):
        raise ValueError("Invalid unit. Please enter C or F.")

      # Perform conversion
      if source_unit == "c":
        converted_value = value * 9/5 + 32
      else:
        converted_value = (value - 32) * 5/9

      # Display result
      print(f"{value}{source_unit.upper()} is equal to {converted_value:.2f}{target_unit.upper()}.")
      break
    except ValueError as e:
      print(e)
      print("Please enter valid inputs.")

def length_converter():
  """
  Converts between meters and feet.
  """
  while True:
    try:
      # Get user input
      value = float(input("Enter the length: "))
      source_unit = input("Enter the source unit (m or ft): ").lower()
      target_unit = input("Enter the target unit (m or ft): ").lower()

      # Validate units
      if source_unit not in ("m", "ft") or target_unit not in ("m", "ft"):
        raise ValueError("Invalid unit. Please enter m or ft.")

      # Perform conversion
      if source_unit == "m":
        converted_value = value * 3.28084
      else:
        converted_value = value / 3.28084

      # Display result
      print(f"{value}{source_unit.upper()} is equal to {converted_value:.2f}{target_unit.upper()}.")
      break
    except ValueError as e:
      print(e)
      print("Please enter valid inputs.")

def weight_converter():
  """
  Converts between kilograms and pounds.
  """
  while True:
    try:
      # Get user input
      value = float(input("Enter the weight: "))
      source_unit = input("Enter the source unit (kg or lb): ").lower()
      target_unit = input("Enter the target unit (kg or lb): ").lower()

      # Validate units
      if source_unit not in ("kg", "lb") or target_unit not in ("kg", "lb"):
        raise ValueError("Invalid unit. Please enter kg or lb.")

      # Perform conversion
      if source_unit == "kg":
        converted_value = value * 2.20462
      else:
        converted_value = value / 2.20462

      # Display result
      print(f"{value}{source_unit.upper()} is equal to {converted_value:.2f}{target_unit.upper()}.")
      break
    except ValueError as e:
      print(e)
      print("Please enter valid inputs.")

# Main program
print("Welcome to the Unit Converter!")
print("Please choose the type of conversion you want to perform:")
print("1. Temperature (Celsius to Fahrenheit and vice versa)")
print("2. Length (Meters to Feet and vice versa)")
print("3. Weight (Kilograms to Pounds and vice versa)")

choice = int(input("Enter your choice: "))

if choice == 1:
  temperature_converter()
elif choice == 2:
  length_converter()
elif choice == 3:
  weight_converter()
else:
  print("Invalid choice. Please try again.")

print("Thank you for using the Unit Converter!")