from datetime import datetime
from model_user import User

class Post:
    next_post_id = 10000

    # using type 'hint' for author, documentation purposes only
    def __init__(self, author: User, title, body):
        self.post_id = Post.next_post_id
        Post.next_post_id += 1
        # DATE string-format-time,  DD/MM/YYYY HH:MM:SS
        self.date_pub = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
        self.author = author
        self.title = title
        self.body = body

    def __str__(self):
        return f""" ------------------------------------   
|     title:  {self.title}  (#{self.post_id})
| published:  {self.date_pub}
|    author:  {self.author.username}
|\n| {self.body}
 ------------------------------------\n"""


# ---------------------------------------------
# FOR DEVELOPMENT AND TROUBLESHOOTING
# ---------------------------

# user1 = User(
#     email="leejenkins@gmail.com",
#     phone="0419111222",
#     fname="Leeroy",
#     lname="Jenkins",
#     username="lee_roooooy",
#     password="HowdyNeighbourYeeharr",
# )

# post1 = Post(
#     author=user1, title="First Post", body="This is the body of the first post"
# )

# print(user1)
# print(post1)