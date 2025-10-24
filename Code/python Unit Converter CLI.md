Build a command-line tool that converts between
Celsius↔Fahrenheit, km↔miles, and kg↔lb.\

def celsius_to_fahrenheit(celsius):

    return celsius * 9 / 5 + 32

  

def kilometers_to_miles(km):

    return km * 0.621371

  

def kilograms_to_pounds(kg):

    return kg * 2.20462

  

def get_numeric_input(prompt):

    while True:

        user_input = input(prompt)

        try:

            return float(user_input)

        except ValueError:

            print(" ОError: Please enter a valid number..")

  

def main():

    while True:

        print("\n===== Unit Converter =====")

        print("1. Degrees Celsius → Fahrenheit")

        print("2. Kilometers → Miles")

        print("3. Kilograms → Pounds")

        print("4. Exit")

  

        choice = input("Select an option (1-4): ")

  

        if choice == "1":

            c = get_numeric_input("Enter the temperature in °C: ")

            f = celsius_to_fahrenheit(c)

            print(f"{c:.2f}°C = {f:.2f}°F")

  

        elif choice == "2":

            km = get_numeric_input("Write the distance in kilometers: ")

            miles = kilometers_to_miles(km)

            print(f"{km:.2f} км = {miles:.2f} миль")

  

        elif choice == "3":

            kg = get_numeric_input("Write down the weight in kg: ")

            pounds = kilograms_to_pounds(kg)

            print(f"{kg:.2f} кг = {pounds:.2f} фунтов")

  

        elif choice == "4":

            print("Exiting the program.")

            break

  

        else:

            print("select an option from 1 to 4.")

  

if __name__ == "__main__":

    main()