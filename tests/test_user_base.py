from unittest import TestCase

from botik.user.user_base import UserBase


class TestUserBase(TestCase):
    def test_add_and_get(self):
        capacity = 10

        user_base = self._make_user_base(capacity)
        users = self._make_users(user_base, capacity)

        for user in users:
            self.assertEqual(user_base.get(user.id), user)

    def test_get_non_existing(self):
        user_base = self._make_user_base(2)
        self._make_users(user_base, 2)

        missing_user = user_base.get(100)
        self.assertEqual(missing_user, None)

    def _make_users(self, user_base, count):
        users = []
        for i in range(count):
            user_base.add(i)
            user = user_base.get(i)
            users.append(user)
        return users

    def _make_user_base(self, capacity):
        return UserBase(capacity)
