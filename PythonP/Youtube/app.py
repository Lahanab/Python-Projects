
tasks = [] #empty list

while True:
    user = input("Enter your task: ")
    if user.lower() == "quit":
        break
    tasks.append(user)
print(tasks)