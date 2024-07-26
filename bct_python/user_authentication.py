class AuthenticationSystem:
    def __init__(self):
        self.users = {}
    def register(self,username,password):
        if username in self.users:
            raise ValueError("Username already exists")
        self.users[username] = password
        print(f"User '{username}' registered successfully")
    def sign_in(self,username,password):
        if username not in self.users:
            raise ValueError("Username not found")
        if self.users[username] != password:
            raise ValueError("Incorrect password")
        print(f"User '{username}' signed in successfully")
        return True
    def show_data(self):
        print("All data of ragisters users :- \n")
        print(self.users)
auth_system = AuthenticationSystem()
while(1):
    n = int(input("press 1 for register\npress 2 for sign in\npress 3 for display register user data\npress 4 for exit\nenter your choice :-"))
    if(n==1):
        try:
            name = input("ENTER THE NAME :- ")
            pas = input("ENTER THE PASSWORD :- ")
            auth_system.register(name, pas)
        except ValueError as e:
            print(e)
    elif(n==2):
        try:
            name = input("ENTER THE NAME :- ")
            pas = input("ENTER THE PASSWORD :- ")
            auth_system.sign_in(name, pas)
        except ValueError as e:
            print(e)
    elif(n==3):
        try:
            auth_system.show_data()
        except ValueError as e:
            print(e)
    elif(n==4):
        break
    else:
        print("wrong choice enter the correct one")