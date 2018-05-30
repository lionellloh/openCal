__author__ = "lionell"

from models.post import Post
from database import Database
from models.blog import Blog

Database.initialize()

blog = Blog(author = "Lionell", title = "I love Nao", description = "hehehehe")

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())
