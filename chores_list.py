task=4
temp_count= task
print(f"You have {temp_count} chores to finish today\n")
completed=0
task_num=1
while task_num<=task:
    if task_num==1: next_task= "Make your bed"
    elif task_num==2: next_task= "Feed the pet"
    elif task_num==3: next_task= "Take out the trash"
    else: next_task= "Wash the dishes"
    ans=input(f"Have you finished: {next_task}? Yes/No")
    if ans=="yes":
        completed= completed+1
        task_num=task_num+1
        print("Great job, task completed")
    else:
        print("Okay, finish it and check again")
    print("Task pending: ",task-completed)
    print()
print("============ALL TASKS COMPLETE=============")
print("Great work finishing your entire checklist today\n")
print("Now lets safely peek at an infinite loop")
test_val=0
safety_con=0
while test_val<=0:
    print("This condition never changes, so this would run forever")
    safety_con=safety_con+1
    if safety_con==3:
        print("(Stopping here on purpose-a real infinite loop never stops on it's own)")
        break

print("=====TASK CHECKLIST SUMMARY=====")
print("Task assigned today",temp_count)
print("Tasks completed",completed)
print("Task pending",task-completed)
print("================================================")