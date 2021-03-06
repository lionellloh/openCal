import uuid
from models.post import Post
import datetime
from database import Database

class Blog(object):

    def __init__(self, author, title, description, _id = None):
        self.author = author
        self.title = title
        self.description = description
        self._id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter Post title:")
        content = input("Enter Post content:")
        date = input("Enter post data or leave blank for today (in format DDMMYYYY):")
        if not date:
            date = datetime.datetime.utcnow()

        else:
            date = datetime.datetime.strptime(date,"%d%m%Y")
        post = Post(blog_id=self._id,
                    title = title,
                    content = content,
                    author = self.author,
                    date = date)

        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self._id)

    def save_to_mongo(self):
        Database.insert(collection="blogs", data = self.json())

    def json(self):
        return {
            'author': self.author,
            'title': self.title ,
            'description': self.description,
            '_id': self._id

        }

    @classmethod
    def from_mongo(cls, _id):
        blog_data = Database.find_one(collection = 'blogs', query = {"id": id})

        return cls(author = blog_data['author'],
                    title = blog_data['title'],
                    description=blog_data['description'],
                    id= blog_data['id'])


