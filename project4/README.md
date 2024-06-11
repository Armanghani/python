User Authentication and Resource Management System


Introduction
This project implements a simple user authentication system and a resource management system using the Factory design pattern and Proxy design pattern. Users can create accounts, log in, and interact with a resource (e.g., reading, writing, and modifying data) through a proxy that handles authentication.

Features
User account creation with password hashing
User login with hashed password verification
Saving and loading user data from a file
Resource interaction through a proxy that checks user authentication
Prerequisites
Python 3.x


ًRpository
https://github.com/Armanghani/python/tree/master/project4


Usage
Run the main script:


python Main.py
The script will create user accounts, save them to a file, and then allow users to log in and interact with the resource.

Project Structure
UserAuthentication.py: Contains the UserAuthentication class that handles account creation, login, and user data management.
ConcreteResource.py: Contains the ConcreteResource class that represents the actual resource users can interact with.
ProxyResource.py: Contains the ProxyResource class that acts as a proxy for the ConcreteResource, handling user authentication before allowing access.
Main.py: The main script that demonstrates the functionality of the system.


Classes and Methods
UserAuthentication
__init__(self): Initializes the user authentication system with an empty dictionary of users.
create_account(self, username, password): Creates a new user account with a hashed password.
login(self, username, password): Verifies the user's login credentials.
push_users(self): Saves the user data to a file.


ConcreteResource
read(self): Simulates reading data from the resource.
write(self, data): Simulates writing data to the resource.
modify(self, data): Simulates modifying data in the resource.


ProxyResource
__init__(self, concrete_resource, user_file): Initializes the proxy with a reference to the concrete resource and a user data file.
read(self, username, password): Authenticates the user and allows reading the resource.
write(self, username, password, data): Authenticates the user and allows writing to the resource.
modify(self, username, password, data): Authenticates the user and allows modifying the resource.

Contributing
Feel free to submit issues, fork the repository, and send pull requests. Contributions are welcome!