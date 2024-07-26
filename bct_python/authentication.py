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
auth_system = AuthenticationSystem()
try:
    auth_system.register("allice","password123")
    auth_system.register("bob","mypassword")
except ValueError as e:
    print(e)
try:
    auth_system.sign_in("allice","password123")
    auth_system.sign_in("bob","wrongpassword")
except ValueError as e:
    print(e)
try:
    auth_system.register("allice","newpassword")
except ValueError as e:
    print(e)
try:
    auth_system.sign_in("charlie","password123")
except ValueError as e:
    print(e)
