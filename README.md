## REDIDIT, reddit .. redid

social media posting platform
post/comment/like/dislike
index page shows last 20 posts, chronologically ordered, 
comments numbered but not shown/expanded unless toggled
users have a profile (viewable by other users)
users have a key-combination (username:password)
allowing control over that profile's 

developement by: Ethan, Christian

using Python on a Django framework

(later) connect to a database for storing posts and comments

(later) connect to third-party cloud storage to store user.image uploads

### To-Do:

User
- create method to allow user to delete their User

Post
- create method to allow user to create Post
- create method to allow user to edit Post
  - post must display a last-modified date/time
  - restrict which fields can be modified (i.e. cannot edit date published or user)

Comment
- comments can be made on a Post, Post.comments = [],
- but no comments sub-thread off other comments (for now)
- one Post can have several Comment instances
- like/dislike function and count
