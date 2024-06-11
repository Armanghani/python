import hashlib

class UserAuthentication:
    def __init__(self):
        self.users = {}

    def create_account(self, username, password):
        if username in self.users:
            return "User already exists"
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.users[username] = hashed_password
        return "Account created successfully"

    def login(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if self.users.get(username) == hashed_password:
            return "Login successful"
        else:
            return "Invalid username or password"

    def push_users(self):
        print("Users to be written to file:", self.users)  # Debugging print statement
        with open("users.txt", 'w') as file:
            for username, hashed_password in self.users.items():
                file.write(f"{username}:{hashed_password}\n")
        return "users.txt"