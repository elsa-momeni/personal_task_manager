import os
from dotenv import load_dotenv
load_dotenv()
admin_password = os.getenv("TASK_MANAGER_ADMIN_PASSWORD")

open_admin = input("do u want to open amin mode? yes/no: ")

if open_admin.lower() == "yes":
    entered_password = input("enter admin password: ")

    if entered_password == admin_password:
        print("admin! hi....")
    else:
        print("wrong password")

name = input("whats your name ?")
print("welcome", name)

priority = input("Enter task priority (low/medium/high): ")

if priority.lower() in ["low", "medium", "high"]:
    print("Priority:", priority.lower())
else:
    print("Invalid priority!")

with open("tasks.txt", "a") as file:
    file.write(f"{name} - Priority: {priority.lower()}\n")