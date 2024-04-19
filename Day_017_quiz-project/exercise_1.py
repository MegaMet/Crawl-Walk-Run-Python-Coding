class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

        print(f"New user: {username}, id: {user_id} is being created...")


    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(user_id="001",username= "Apple")
user_2 = User(user_id="002",username= "Orange")

print(user_1.username)