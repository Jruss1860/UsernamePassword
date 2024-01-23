full_storage = []
stored_stuff = []



print("---------------------------------------------------------")
print("Welcome to my storage center for usernames and passwords!")
print("---------------------------------------------------------")

user = input("Enter a username. ")
full_storage.append(user)

print (f"You successfully added the username {user}")

password = input("Enter a password. ")
full_storage.append(password)
print (f"You successfully added the passcode {password}")


print_name = input ("Would you like to print your username and passwords? Y/N: ")
if print_name == "y" or "Y":
    print(f"{full_storage}")






