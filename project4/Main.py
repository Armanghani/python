from ConcreteResource import ConcreteResource
from ProxyResource import ProxyResource
from UserAuthentication import UserAuthentication

def main():
    resource = ConcreteResource()
    auth = UserAuthentication()
    proxy = ProxyResource(resource,auth)

    # Create accounts
    print(auth.create_account("user1", "password1"))
    print(auth.create_account("user2", "password2"))

    # Login and interact with the resource
    username = "user1"
    password = "password1"
    auth.login(username, password)
    print(proxy.read(username, password))
    print(proxy.write(username, password, "New Data"))
    print(proxy.modify(username, password, " Modified"))
    print(resource.read())

if __name__ == "__main__":
    main()