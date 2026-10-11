age = int(input("how old are you ?"))
print("you are", age ,"years old")

country = input("where are you from? ")
print("you are from", country)
with open("tasks.txt", "a") as file:
    file.write(f"{age} - {country} - ")