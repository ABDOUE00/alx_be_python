# daily_reminder.py

def main():
    # Prompt for user input
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()  # Convert to lowercase for case insensitivity
    time_bound = input("Is it time-bound? (yes/no): ").lower()  # Convert to lowercase for case insensitivity
    
    # Match Case statement for priority
    match priority:
        case 'high':
            reminder = f"'{task}' is a high priority task"
        case 'medium':
            reminder = f"'{task}' is a medium priority task"
        case 'low':
            reminder = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority input. Please enter high, medium, or low.")
            return
    
    # Check if the task is time-bound
    if time_bound == 'yes':
        reminder += " that requires immediate attention today!"
    elif time_bound == 'no':
        reminder += ". Consider completing it when you have free time."
    else:
        print("Invalid input for time-bound. Please enter yes or no.")
        return
    
    # Print the reminder message
    print("Reminder:", reminder)

if __name__ == "__main__":
    main()
