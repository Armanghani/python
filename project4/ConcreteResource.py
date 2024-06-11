from InterfaceResource import Resource

class ConcreteResource(Resource):
    def __init__(self):
        self.data = "Initial Data"

    def read(self):
        return self.data

    def write(self, data):
        self.data = data
        return "Data written successfully"

    def modify(self, data):
        self.data += data
        return "Data modified successfully"