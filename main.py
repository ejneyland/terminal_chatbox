import sys
from model_user import User
from model_post import Post

# from model_comment import Comment
from operation_user import UserOperation
from operation_post import PostOperation

# from operation_comment import CommentOperation

#   ^^^^^ imports ^^^^^

# booleans
# user_in_session = False

# initialise a list of [User] and [Post]
users = []
posts = []

# initialise Post and User Operations
post_ops = PostOperation()
user_ops = UserOperation()

# creating three User instances
user1 = User(
    email="leejenkins@gmail.com",
    phone="0419111222",
    fname="Leeroy",
    lname="Jenkins",
    username="lee_roooooy",
    password="HowdyNeighbourYeeharr",
)

user2 = User(
    email="friendlyneighbour@hotmail.com",
    phone="0413222333",
    fname="Mary",
    lname="Jane",
    username="mary_jane_xx",
    password="iHeartPeterParker",
)
user3 = User(
    email="suzanne@outlook.com",
    phone="0409333444",
    fname="Big",
    lname="Suze",
    username="sophisticatedwoman",
    password="luckyPASSWORD13579",
)
user4 = User(
    email="daisythomas@gmail.com",
    phone="0413777999",
    fname="Daisy",
    lname="Thomas",
    username="daisy_chain",
    password="Collingwood2010",
)

user5 = User(
    email="thegtrain@gmail.com",
    phone="0412345678",
    fname="Fraser",
    lname="Gehrig",
    username="tootTooT_itsthe_GTrain",
    password="549$snags",
)

# print(user5.username)

user_ops.update_user_username(user5, "tootoot_its_gtrain")
user_ops.update_user_phone(user5, "1800 GTRAIN")

# append users to the users[] list
users.append(user1)
users.append(user2)
users.append(user3)
users.extend([user4, user5])  # 'extend' appends multiple items

# creating three Post instances, one for each User
post1 = Post(
    author=user1, title="First Post", body="This is the body of the first post"
)
post2 = Post(
    author=user2, title="Second Post", body="This is the body of the second post"
)
post3 = Post(
    author=user3, title="Third Post", body="This is the body of the third post"
)

# append posts to the posts[] list
posts.append(post1)
posts.append(post2)
posts.append(post3)


# checks that the username input exists in the list of users[User]
def check_username_exists(users: list[User], input_username):
    for user in users:
        if user.username == input_username:
            print(f"User '{input_username}' found")
            return True
    print(f"User of username '{input_username}' cannot be found in the system.")
    return False


# print(check_username_exists(users=users, input_username="lee_roooy"))
# print(check_username_exists(users=users, input_username="tootoot_its_gtrain"))
# print(check_username_exists(users=users, input_username="tootTooT_itsthe_GTrain"))


def login_input(users: list[User], reg_username=None):
    user_exists = check_username_exists(users, reg_username)
    # user_exists = any(user.username == reg_username for user in users)
    if reg_username is not None and user_exists:
        print(f"Login for user: {reg_username}")
        password = input("Password:  ")
        return reg_username, password
    else:
        username = input("Please enter your username:  ")
        password = input("Password:  ")
        return username, password


# print(login_input(users, reg_username="exampleuser1200"))

# log_username, log_password = login_input(users, reg_username="tootoot_its_gtrain")  # pw: 549$snags

# print(f"username given: {log_username}, \npassword given: {log_password}")


def register_input():
    fname = input("Please enter your First Name:  ")
    lname = input("Please enter your Family Name:  ")
    email = input("Email address:  ")
    phone = input("Phone number:  ")
    username = input("Please assign a username:  ")
    password = ""

    new_pw = True
    while new_pw:
        set_pw = input("Please enter a new password:  ")

        inner_loop = True
        while inner_loop:
            check_pw = input(
                "Please confirm your password:  \n(or enter B, to go Back and set a new password)\n"
            )

            if check_pw == set_pw:
                password = set_pw
                print("Confirmed. Password successfully created.")
                return fname, lname, email, phone, username, password
            elif check_pw.strip()[0].capitalize() == "B":
                inner_loop = False
            else:
                print("Passwords did not match.")


fname, lname, email, phone, username, password = register_input()

print(fname, lname, email, phone, username, password)

# # test login
# while True:
#     login_choice = input(
#         "Would you like to Register, Login, or Exit? \nEnter R, L, or X .. \n "
#     ).strip()
#     if login_choice.capitalize()[0] == "R":
#         print("Register new User:  ")
#         # registration input retrieves required new User data (and validated (later))
#         fname, lname, email, phone, username, password = register_input()
#         new_user = User(
#             email=email,
#             phone=phone,
#             fname=fname,
#             lname=lname,
#             username=username,
#             password=password,
#         )
#         if new_user:
#             users.append(new_user)
#             login_choice = "R"
#             print(
#                 "User successfully registered. Please Login now, using your credentials"
#             )

#     elif login_choice.capitalize()[0] == "L":
#         print("User Login:  ")
#         username, password = login_input()
#         logged_in_user = user_ops.login(users, username, password)
#         if logged_in_user:
#             user_in_session = True
#         else:
#             print("Unsuccessful Login.")
#     elif login_choice.capitalize()[0] == "X":
#         sys.exit()
#     else:
#         print(
#             "Invalid selection. Please select either: R or L, \n for Register (new users) and Login (existing users). \n X for Exit"
#         )

# user_signed_in = user_ops.login(users, "mary_jane_xx", "iHeartPeterParker")
