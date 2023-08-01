name =input("Enter your fullname: ")
mobile =input("Enter your mobile number (in this format 05x-xxxx-xxx): ")
birth_year = int(input("Enter your year of birth: "))

current_year =2023

age =current_year - birth_year

mobile_list = mobile.split("-")
print (f"Your name is: {name}")
print (f"Your age is: {age}")
print(mobile_list)


