from src.common.database import Database
import uuid
import datetime

__author__ = "Lionell"



class Post(object):

    def __init__(self, blog_id, title, content, author, created_date = datetime.datetime.utcnow(), _id = None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = created_date

        # Every post is unique with this class variable
        self._id = uuid.uuid4().hex if _id is None else _id


    def save_to_mongo(self):
        Database.insert(collection = "posts",
                        data = self.json())

    def json(self):
        json_rep = {
            "id": self._id,
            "title" : self.title,
            "content": self.content,
            "author": self.author,
            "created_date": self.created_date,
            "blog_id": self.blog_id

        }

        return json_rep

    # Given a post id, return the post
    @classmethod
    def from_mongo(cls, id):
        # Post.from_mongo(id)
        post_data = Database.find_one(collection = "posts", query = {"id":id})
        return cls(**post_data)

    # Given a blog id, return all the posts in that blog
    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection = "posts", query = {"blog_id": id})]
