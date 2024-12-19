# Beginning
summer_points = 0
winter_points = 0
# Middle
answer = input("Would you rather A) go to the beach, or B) go skiing")
if answer == "A":
    summer_points += 1
elif answer == "B":
    winter_points += 1

answer = input("Would you rather A) go on a hike, or B) go on a walk in the woods with snowshoes")
if answer == "A":
    summer_points += 1
elif answer == "B":
    winter_points += 1

answer = input("Would you rather A) go in a pool, or B) go in a hot tub")
if answer == "A":
    summer_points += 1
elif answer == "B":
    winter_points += 1

answer = input("Would you rather A) go surfing, or B) go sledding")
if answer == "A":
    summer_points += 1
elif answer == "B":
    winter_points += 1

answer = input("Would you rather A) get ice cream, or B) get hot cocoa")
if answer == "A":
    summer_points += 1
elif answer == "B":
    winter_points += 1
# End
if summer_points > winter_points:
    print("You are a summer person")
elif winter_points > summer_points:
    print("You are a winter person")