import bcrypt
from datetime import datetime

class User:
    existing_ids = set()
    next_user_id = 100

    def __init__(self, email, phone, fname, lname, username, password):
        self.user_num = User.next_user_id
        User.next_user_id += 1
        # DATE string-format-time,  DD/MM/YYYY HH:MM:SS
        self.date_sub = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
        self.email = email
        self.phone = phone
        self.fname = fname
        self.lname = lname
        self.username = username
        self.encrypted_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        self.logged_in = False

    def __str__(self):
        return f"""   user:  {self.username} (#{self.user_num})
   name:  {self.fname} {self.lname}
  email:  {self.email}
  phone:  {self.phone}
created:  {self.date_sub}"""


# ---------------------------------------------
# FOR DEVELOPMENT AND TROUBLESHOOTING
# ---------------------------

# ethan = User(
#     email="ethan@gmail.com",
#     phone="0412999777",
#     fname="Ethan",
#     lname="Neyland",
#     username="ejneyland",
#     password="SimplePassword123!",
# )

# print(ethan.encrypted_pw)


# # login verification
# provided_password = "SimplePassword123!"
# if bcrypt.checkpw(provided_password.encode("utf-8"), ethan.encrypted_pw):
#     print("Login successful")
# else:
#     print("Invalid password")
