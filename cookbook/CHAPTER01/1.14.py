"""기본 비교 기능 없이 객체 정렬"""
from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]
print(users)
print('lambda:', sorted(users, key=lambda u: u.user_id))
print('attrgetter:', sorted(users, key=attrgetter('user_id')))

#
print(sorted(users, key=attrgetter('user_id')))

#
print(min(users, key=attrgetter('user_id')))
print(max(users, key=attrgetter('user_id')))
