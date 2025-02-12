from models.user import User

class User_Service:
    def __init__(self):
        self.user = {}

    def add_user(self, id,name,email):
        user = User(name,id,email)
        self.user[id] = user
        return user