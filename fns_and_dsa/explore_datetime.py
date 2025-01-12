from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in the format YYYY-MM-DD HH:MM:SS.
    """
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    """
    Calculate and display the date after a specified number of days from today.
    """
    try:
        # Prompt user for number of days
        days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
        print("Future Date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter an integer.")

def main():
    """
    Main function to demonstrate the usage of the datetime module.
    """
    print("Datetime Exploration Script")
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
