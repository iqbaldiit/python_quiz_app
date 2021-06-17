import user

class Login():
    def __init__(self):
        self.email=""
        self.password=""
        pass

    def login(self):
        sUser=user.User()
        validUser=list(sUser.getUser())
        if (validUser.count>0):
            return True
        else:
            return False

        