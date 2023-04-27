from os import system


def activity():
    # Asks users for their activity level. 
    print("Please check the list below and choose the option that best describes you:")
    levels = ["\n1. Not Very Active. Spend most of the day sitting (e.g. bank teller, desk job)",
              "\n2. 'Lightly Active', 'Spend a good part of the day on your feet (e.g. teacher, salesperson)"
              "\n3. Active. Spend a good part of the day doing some physical activity "
              "(e.g. food server, postal carrier)",
              "\n4. Very Active. Spend most of the day doing some physical activity "
              "(e.g. bike, messenger, carpenter)"
              ]
    for level in levels:
        print(level)
    activity_pick = False
    while not activity_pick:
        activity_pick = int(input("\nWhat is your level of activity (1-4) ? "))
        if activity_pick not in range(1, 5):
            print("Invalid input. Please enter a number from 1 to 4.")
            activity_pick = False
        else:
            activity_pick = True
    activity_pick -= 1
    activity_pick = levels[activity_pick]
    system("clear")
    print(f"\nYour activity level '{activity_pick[4:]}' is now set!\n"
          f"You're one step closer to achieving your goals!")
    print(activity_pick)
    return activity_pick


def goals():
    # Asks users for their goals
    print("Let's start with your goals!")
    print("Please check the list below and insert your selection (1-7)")
    goals_lst = ["1. Lose Weight", "2. Maintain Weight", "3. Gain weight", "4. Gain Muscle", "5. Modify My Diet",
                 "6. Manage Stress", "7. Increase Step Count \n"]
    for goal in goals_lst:
        print(goal)
    user_pick = False
    while not user_pick:
        user_pick = int(input("Your selection (1-7): "))
        if user_pick not in range(1, 8):
            print("Invalid input. Please enter a number from 1 to 7.")
            user_pick = False
        else:
            user_pick = True
    user_pick -= 1
    user_pick = goals_lst[user_pick]
    system("clear")
    print(f"Great! Your goal to {user_pick[3:]} is now set!\n"
          f"You've just taken a big step on your journey.")
    print("\nNow, let's talk about your activity level 💪\n")
    activity()


if __name__ == "__main__":
    goals()
