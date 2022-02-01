from bot_config import NUMBER_OF_USERS, MAX_POSTS_PER_USER, MAX_LIKES_PER_USER
import random


def infinite_file_generator(filename):
    f = open(filename)
    while True:
        try:
            yield f.__next__().strip()
        except:
            f.seek(0)
            continue


def usernames_generator():
    yield from infinite_file_generator('random_usernames.txt')


def post_messages_generator():
    yield from infinite_file_generator('random_post_messages.txt')


class Bot:
    def __init__(self):
        self.usernames_generator = usernames_generator()
        self.post_messages_generator = post_messages_generator()
        self.users = []
        self.posts = []

    def signup_users(self, number_of_users):
        signed_up_users = 0
        for username in self.usernames_generator:

            if signed_up_users == number_of_users:
                break

            self._signup_user(username)
            self._save_user(username)
            signed_up_users += 1

    def _signup_user(self, username):
        pass

    def _save_user(self, username):
        pass

    def create_random_number_of_posts_per_user(self, max_posts_per_user):
        for user in self.users:
            number_of_posts = random.randint(1, max_posts_per_user)
            for post_index in range(number_of_posts):
                post = self._create_random_post(user)
                self._save_post(post)

    def _create_random_post(self, user):
        pass

    def _save_post(self, post):
        pass

    def authenticate_users(self):
        for user in self.users:
            authenticated_user = self._authenticate_user(user)
            self._save_user(authenticated_user)

    def _authenticate_user(self, user):
        pass

    def randomly_like_posts(self, max_likes_per_user):
        for user in self.users:
            number_of_likes = random.randint(1, max_likes_per_user)
            for like_index in range(number_of_likes):
                random_post = random.choice(self.posts)
                self._like_post(user, random_post)


#bot = Bot()
#bot.signup_users(NUMBER_OF_USERS)
#bot.authenticate_users()
#bot.create_random_number_of_posts_per_user(MAX_POSTS_PER_USER)
#bot.randomly_like_posts(MAX_LIKES_PER_USER)