# try to create a basic password keeper


user = input('your name?: ')
print(f'hey {user}! welcome to WTFH( "[W]hat [T]he [F]uck is [H]acking)": !')

ask = int(input('for how many sites you have to store passwords :'))
manager = {}

for i in range(ask):
    print(f"\n--- Site{i+1}---")

    ask_site = input(f"Mention the Site: ")
    ask_pass = input(f"Mention the Pass: ")

    manager[i + 1] = {"site": ask_site, "pass": ask_pass} 


user_pass = input("Do you want to retrive your password [y] or [n]?: ")

if user_pass == "y":
    print(f"You stored your password for {manager} times.")

elif(user == 'n'):
    print(f'No worries {user}')

else:
    print('Wrong option enterd by User !')

    


