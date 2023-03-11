from os import system

def activity():
    activity_lvl = input("\nWhat is your level of activity (1-4) ? ")
    levels = ["1. Not Very Active. Spend most of the day sitting (e.g. bank teller, desk job)\n",
              "2. Lightly Active. Spend a good part of the day on your feet (e.g. teacher, salesperson)\n",
              "3. Active. Spend a good part of the day doing some physical activity "
              "(e.g. food server, postal carrier)\n",
              "4. Very Active. Spend most of the day doing some physical activity "
              "(e.g. bike, messenger, carpenter)\n"
              ]
    print("\nHere are the activity levels:")
    for level in levels:
        print(level)


class Goals:

    def __init__(self, user_pick=None):
        """ Asks users for their goals """
        print("Let's start with your goals!")
        print("Please select your goal from the list above (1-7)")
        goals = ["1. Lose Weight", "2. Maintain Weight", "3. Gain weight", "4. Gain Muscle", "5. Modify My Diet",
                 "6. Manage Stress", "7. Increase Step Count \n"]
        for goal in goals:
            print(goal)
        user_pick = None
        while user_pick not in range(1, 8):
            try:
                user_pick = int(input("Your selection (1-7): "))
            except ValueError:
                print("Invalid input. Please enter a number from 1 to 7.")
        user_pick -= 1
        self.user_pick = user_pick
        system("clear")
        print(f"Great! Your goal to {goals[self.user_pick]} is now set!\n"
              f"You've just taken a big step on your journey.")
        print("\nNow, let's talk about your activity level 💪")
        activity()


test = Goals()
print(test)
