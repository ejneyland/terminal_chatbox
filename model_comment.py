from model_user import User
from model_post import Post
from datetime import datetime


class Comment:
    # using type 'hint' for author, documentation purposes only
    def __init__(self, post: Post, author: User, body):
        self.post_id = post.post_id
        self.comm_auth = author.username
        self.body = body
        self.date_posted = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
        self.num_of_likes = 0
        self.num_of_dislikes = 0

    def __str__(self):
        return f"""replying to: post #{self.post_id}
    {self.comm_auth}
    {self.body}
    {self.date_posted}
{self.num_of_likes} 👍🏽    {self.num_of_dislikes} 👎🏽
        """


# ---------------------------------------------
# FOR DEVELOPMENT AND TROUBLESHOOTING
# ---------------------------

# comm1 = Comment()