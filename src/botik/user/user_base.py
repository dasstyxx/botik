from botik.user.user import User


class UserBase:
    """
    A store of id mappings to a User object.
    """

    def __init__(self):
        self.users = {}

    def add(self, user_id):
        user = User(user_id)
        self.users[user_id] = user
        return user

    def get(self, user_id):
        if not self.exists(user_id):
            return None

        return self.users.get(user_id)

    def exists(self, user_id):
        return user_id in self.users
