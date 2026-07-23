list_of_tasks = []

def main():
    while True:
        task_input = input("Enter a task you need to do: ")
        
        if task_input == "":
            task_count = len(list_of_tasks)
            print(list_of_tasks)
            print("No more tasks need to be listed.")
            print("You have a total of", task_count, "tasks to complete.")
            break
        else:
            list_of_tasks.append(task_input)
            continue

main()