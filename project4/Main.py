from ConcreteResource import ConcreteResource
from ProxyResource import ProxyResource
from UserAuthentication import UserAuthentication

def main():
    resource = ConcreteResource()
    auth = UserAuthentication()
    
    # Create accounts
    print(auth.create_account("user1", "password1"))
    print(auth.create_account("user2", "password2"))
    
    # Check users in memory before saving to file
    print("Users in memory:", auth.users)  # Debugging print statement
    
    # Save users to file
    user_auth_file = auth.push_users()
    
    # Initialize proxy with user file
    proxy = ProxyResource(resource, user_auth_file)
    
    # Login and interact with the resource
    username = "user1"
    password = "password1"
    print(auth.login(username, password))
    print(proxy.read(username, password))
    print(proxy.write(username, password, "New Data"))
    print(proxy.modify(username, password, " Modified"))

if __name__ == "__main__":
    main()