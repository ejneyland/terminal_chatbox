import bcrypt
from model_user import User

users = []


class UserOperation:
    @staticmethod
    def capture_signup_data():
        input()

    def create_user(
        self,
        input_email,
        input_phone,
        input_fname,
        input_lname,
        input_username,
        input_password,
    ):
        new_user = User(
            email=input_email,
            phone=input_phone,
            fname=input_fname,
            lname=input_lname,
            username=input_username,
            password=input_password,
        )
        return new_user

    def read_user(self, user: User):
        print(user)
        # return user

    def login(self, users, input_username, input_password):
        # is users isn't False (isn't empty) the program will continue?
        if users:
            for user in users:
                if isinstance(user, User) and user.username == input_username:
                    if bcrypt.checkpw(input_password.encode("utf-8"), user.encrypted_pw):
                        print("Login successful!")
                        return user
                    else:
                        print("Incorrect password.")
                else:
                    print(f"No user found with username: '{input_username}'.")
        else:
            print("User list is empty.")
            return None

    def update_user_email(self, user: User, new_user_email):
        user.email = new_user_email

    def update_user_phone(self, user: User, new_user_phone):
        user.phone = new_user_phone

    def update_user_fname(self, user: User, new_user_fname):
        user.fname = new_user_fname

    def update_user_lname(self, user: User, new_user_lname):
        user.lname = new_user_lname

    def update_user_username(self, user: User, new_username):
        user.username = new_username


# ---------------------------------------------
# FOR DEVELOPMENT AND TROUBLESHOOTING
# ---------------------------

# user_ops = UserOperation()

# user_ops.login("tootoot_its_gtrain", "549$snags")
