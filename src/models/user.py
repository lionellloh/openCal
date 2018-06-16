# Something that allows our user to login and register
from src.common.database import Database

class User(object):
    def __init__(email, password):
        self.email = email
        self.password = password



    # We do not yet have user object. Hence we cannot use self .email
    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one("users", {"email": email})

        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one("users", {"_id": _id})
        if data is not None
            return cls(**data)


    @staticmethod
    def login_valid(email, password):
        # User.login_valid("lionell@gmail.com", "1234")
        # Chek whether a user's email matches the password they sent us
        user = User.get_by_email(email)
        if user is not None:
            return user.password == password

    @classmethod
    def register(cls, email, password):
        user = cls.get_by_email(email)
        if user is None:
            new_user = cls(email, password)
            new_user.save_to_mongo()
            session['email'] = email
            return True

        else:
            return False

    @staticmethod
    def login(user_email):
        # login_valid has already been called
        # The cookie stores the unique identifier that accesses the session (stored on the server side).
        # The session gives us the email of the user.
        session['email'] = user_email

    @staticmethod
    def logout():
        session['email'] = None


    def get_blogs(self):
        

    # Json output will only be done inside the app
    def json(self):
        return {
            "email": self.email,
            "_id": self._id,
            "password": self.password
        }

    def save_to_mongo(self):
        Database.insert("users", self.json())


