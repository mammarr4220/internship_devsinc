list_of_tasks = []

def main():
    while True:
        task_input = input("Enter a task you need to do: ")
        
        if task_input == "":
            print(list_of_tasks)
            print("No more tasks need to be listed.")
            break
        else:
            list_of_tasks.append(task_input)
            continue
    
main()