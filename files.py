
name = input("Enter your name: ")
age = input("Enter your age: ")
dob = input("Enter your date of birth: ")

user_info = f"Name: {name}\nAge: {age}\nDate of Birth: {dob}"

file_name = "user_info.txt"
with open(file_name, "w") as file:
    file.write(user_info)

print("User information has been saved to", file_name)