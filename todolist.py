print("*******To_Do_list******* ")
print("*******welcome********")
print("choose operation")
Tasks = [ ] #list to save Tasks
while True:
	print("operations: ")
	print("1.Add Task")
	print("2.Show Tasks")
	print("3.Delete Tasks")
	print("4.exit")


	choice = input("choice the operation: ") # take input from user to choice operation

	if choice == "1":
		print("Add task")
		add_task = input("add the task: ")
		Tasks.append(add_task)
	elif choice == "2":
		print("show tasks")
		for i, task in enumerate(Tasks):
			print(i+1, task)
	elif choice == "3":
		print("delete task")
		delete_task = input("Delete task: ")
		Tasks.remove(delete_task)
	elif choice == "4":
		print("exit")
		break
	else:
		print("ERROR")
#++++++soon+++++++:
# TODO: save tasks to file
# TODO: mark task as complete
# TODO: delete by number
