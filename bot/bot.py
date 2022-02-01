from bot_config import NUMBER_OF_USERS, MAX_POSTS_PER_USER, MAX_LIKES_PER_USER
import random
import requests
import json

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
    def __init__(self, api_operations):
        self.usernames_generator = usernames_generator()
        self.post_messages_generator = post_messages_generator()
        self.users = []
        self.posts = []
        self.api_operations = api_operations

    def signup_users(self, number_of_users):
        signed_up_users = 0
        for username in self.usernames_generator:

            if signed_up_users == number_of_users:
                break

            user = self._signup_user(username)
            self._save_user(user)
            signed_up_users += 1

    def _signup_user(self, username):
        user = self.api_operations.signup_user(username, username)
        return user

    def _save_user(self, user_to_add):
        self.users = [user for user in self.users if not user['username'] == user_to_add['username']]
        self.users.append(user_to_add)


    def create_random_number_of_posts_per_user(self, max_posts_per_user):
        for user in self.users:
            number_of_posts = random.randint(1, max_posts_per_user)
            for post_index in range(number_of_posts):
                post = self._create_random_post(user)
                self._save_post(post)

    def _create_random_post(self, user):
        post_message = self.post_messages_generator.__next__()
        post = self.api_operations.create_post(user, post_message)
        return post

    def _save_post(self, post):
        self.posts.append(post)

    def authenticate_users(self):
        for user in self.users:
            authenticated_user = self._authenticate_user(user)
            self._save_user(authenticated_user)

    def _authenticate_user(self, user):
        authenticated_user = self.api_operations.authenticate_user(user)
        return authenticated_user

    def randomly_like_posts(self, max_likes_per_user):
        for user in self.users:
            number_of_likes = random.randint(1, max_likes_per_user)
            for like_index in range(number_of_likes):
                random_post = random.choice(self.posts)
                self._like_post(user, random_post)

class ApiOperations:
    def __init__(self, api_url):
        self.api_url = api_url

    def signup_user(self, username, password):
        payload = {'username' : username, 'password' : password}
        response = requests.post(self.api_url + '/user/', json = payload)
        return payload

    def create_post(self, user, post_message):
        payload = {'post_text' : post_message}
        headers = {'Authorization' : user.get('access_token')}
        response = requests.post(self.api_url + '/post/', json = payload, headers = headers)
        response = json.loads(response.text)
        return {'post_id' : response['post_id']}

    def authenticate_user(self, user):
        payload = {'username': user['username'], 'password': user['password']}
        response = requests.post(self.api_url + '/login/', json=payload)
        response = json.loads(response.text)
        user['access_token'] = response['access_token']
        return user

    def like_post(self, user, post):
        headers = {'Authorization': user.get('access_token')}
        response = requests.post(self.api_url + '/post/{}/like'.format(post['id']), headers=headers)


#bot = Bot()
#bot.signup_users(NUMBER_OF_USERS)
#bot.authenticate_users()
#bot.create_random_number_of_posts_per_user(MAX_POSTS_PER_USER)
#bot.randomly_like_posts(MAX_LIKES_PER_USER)