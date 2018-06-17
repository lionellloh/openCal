# Something that allows our user to login and register
from flask import Flask, session
from src.common.database import Database
from src.models.blog import Blog
import datetime
import uuid

class User(object):
    def __init__(self,_id, email, password):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id



    # We do not yet have user object. Hence we cannot use self .email
    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one("users", {"email": email})
        print(data)
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one("users", {"_id": _id})
        if data is not None:
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
            new_user = cls(None, email, password)
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
        return Blog.find_by_author_id(self._id)

    def new_blog(self, title, description):
    #     We need author, title, description, author_id
    # We do not have any duplication check now
        blog = Blog(author = self.email,
                    title = title,
                    description = description,
                    author_id = self._id)

        blog.save_to_mongo()

    @staticmethod
    def new_post(blog_id, title, content, date = datetime.datetime.utcnow()):
        # Blog_id is derived from the website
        blog = Blog.from_mongo(blog_id)
        blog.new_post(title = title,
                      content = content,
                      created_date = date)



    # Json output will only be done inside the app
    def json(self):
        return {
            "email": self.email,
            "_id": self._id,
            "password": self.password
        }

    def save_to_mongo(self):
        Database.insert("users", self.json())


