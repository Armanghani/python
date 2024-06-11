import hashlib
from InterfaceResource import Resource
from UserAuthentication import UserAuthentication

class ProxyResource(Resource):
    def __init__(self, real_resource,user_auth):
        self.real_resource = real_resource
        self.users = user_auth.push_users()

    def authenticate(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return self.users.get(username) == hashed_password

    def read(self, username, password):
        if self.authenticate(username, password):
            return self.real_resource.read()
        else:
            return "Login was not succesfully!"


    def write(self, username, password, data):
        if self.authenticate(username, password):
            return self.real_resource.write(data)
        else:
            return "Authentication failed"

    def modify(self, username, password, data):
        if self.authenticate(username, password):
            return self.real_resource.modify(data)
        else:
            return "Authentication failed"