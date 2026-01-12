# Cooking Performance Evaluation using function

def evaluate_chef(chef_name, kitchen_name, dish_name, taste, presentation, hygiene):
    # Calculate average score
    average_score = (taste + presentation + hygiene) / 3

    # Assign performance level
    if average_score >= 90:
        performance = "Master Chef"
    elif average_score >= 80:
        performance = "Expert Chef"
    elif average_score >= 65:
        performance = "Skilled Chef"
    elif average_score >= 50:
        performance = "Beginner Chef"
    else:
        performance = "Needs Improvement"

    # Display result
    print("\n--- Cooking Performance Result ---")
    print("Chef Name:", chef_name)
    print("Kitchen Name:", kitchen_name)
    print("Dish Prepared:", dish_name)
    print("Average Score:", round(average_score, 2))
    print("Performance Level:", performance)


# Main program
chef_name = input("Enter Chef Name: ")
kitchen_name = input("Enter Kitchen Name: ")
dish_name = input("Enter Dish Prepared: ")

taste = float(input("Enter Taste Score (0-100): "))
presentation = float(input("Enter Presentation Score (0-100): "))
hygiene = float(input("Enter Hygiene Score (0-100): "))

# Function call
evaluate_chef(chef_name, kitchen_name, dish_name, taste, presentation, hygiene)
