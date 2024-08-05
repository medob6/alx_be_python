task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
x = "Reminder:"
reminder = f" '{task}' is a {priority} priority task"
match priority:
    case "high":
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Make sure to complete it as soon as possible."
    case "medium":
        if time_bound == "yes":
            reminder += " that should be done today."
        else:
            reminder += ". Try to complete it soon."
    case "low":
        if time_bound == "yes":
            reminder += " that should be addressed when possible today."
        else:
            reminder += ". Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority entered. Please enter high, medium, or low."
if time_bound == "no":
    x = "Note:"
print(x,reminder)