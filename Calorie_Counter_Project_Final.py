print("Welcome to Calorie Counter! The app that will tell you how many calories to eat based your personal goal!")
name = input ("Enter name:")
height = float(input ("Enter height in inches:"))
weight = float(input ("Enter weight in lbs:"))
age = float(input ("Enter age:"))
sex = input ("Enter Male or Female:")
calories_per_day_male = 66.47 + 6.24*(weight) + 12.7*(height) - 6.755*age
calories_per_day_female = 655.1 + 4.35*weight + 4.7*height - 4.7*age
if sex.lower() == "male":
    print("Your BMR is estimated to be " + str(calories_per_day_male) + " per day.")
if sex.lower() == "female":
    print("Your BMR is estimated to be " + str(calories_per_day_female) + " per day.")
print("Now let's find out if you want to lose weight or gain weight.")
goal = input ("Enter Lose or Gain:")
if goal.lower() == "gain" and sex.lower() == "male":
    calorie_goal = calories_per_day_male + 500
    print("Your daily calorie goal to gain 1lb a week is " + str(calorie_goal) + ".")
if goal.lower() == "lose" and sex.lower() == "male":
    calorie_goal = calories_per_day_male - 500
    print("Your daily calorie goal to lose 1lb a week is " + str(calorie_goal) + ".")
if goal.lower() == "gain" and sex.lower() == "female":
    calorie_goal = calories_per_day_female + 500
    print("Your daily calorie goal to gain 1lb a week is " + str(calorie_goal) + ".")
if goal.lower() == "lose" and sex.lower() == "female":
    calorie_goal = calories_per_day_female - 500
    print("Your daily calorie goal to lose 1lb a week is " + str(calorie_goal) + ".")
    









