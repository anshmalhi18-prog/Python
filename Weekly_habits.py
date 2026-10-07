habit_info = ("Reading", True, 8, 21.5)
print(habit_info)

weekly_habits= (0,1,1,0,1,1,1)
print(weekly_habits)

print("Total days tracked: ",len(weekly_habits))

print("Day 1 status: ",weekly_habits[0])
print("Day 4 status: ",weekly_habits[4])

first_three_days=weekly_habits[0:3]
print("First three days: ",first_three_days)

weekend_days=weekly_habits[5:7]
print("Weekend Days: ",weekend_days)

weekly_habits=weekly_habits+1
print("After adding one more day: ",weekly_habits)

completed=weekly_habits.count(1)
missed=weekly_habits.count(0)

done=0
not_done=0

for i in range(len(weekly_habits)):
    if weekly_habits[i] == 1:
        done +=1
    else:
        not_done +=1

if done>not_done:
    print("Great progress")

else:
    print("Try to be more consistent")

print("")
print("=====================WEEKLY HABIT TRACKER=======================")
print("Habit Name: ",habit_info[0])
print("Weekly Record: ",weekly_habits)
print("Completed: ",done)
print("Missed: ",not_done)
print("================================================================")