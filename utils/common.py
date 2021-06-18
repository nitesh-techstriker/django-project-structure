import uuid
import requests
import string
import random
from django.core.files.storage import FileSystemStorage
import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator


# import pandas as pd

def get_input_data(request):
    if request.method == 'GET':
        input_data = request.GET
    else:
        input_data = request.data
    return input_data


def generate_response(data=dict, message='', status=200):
    if status == 200 or status == 201:
        status_bool = True
    else:
        status_bool = False

    return {
               'data': data,
               'message': message,
               'status': False
           }, status_bool


def change_file_name(filename):
    extension = filename.split('.')[-1]
    return uuid.uuid4().hex + '.' + extension


def save_files_to_filesystem(file_name, file):
    fs = FileSystemStorage()
    filename = fs.save('sheets/' + file_name, file)
    uploaded_file_url = fs.url(filename)
    return uploaded_file_url


def get_client_ip(request):
    x_forwarded_for = request.remote_addr
    ip = x_forwarded_for.split(',')[0]
    return ip


# TODO get location from ip
def get_location(ip):
    try:
        loc = requests.request("GET", "http://ip-api.com/json/{0}".format(ip)).json()
        print(loc)
        location = loc['city'] + ', ' + loc['country'] + ', ' + loc['countryCode']
    except Exception as e:
        print(e)
        location = "unidentified"

    return location


# def get_user_from_token(request):
#     token = get_token(request)
#     Jwt = JwtAuth(token)
#     user, headers = Jwt.decode()[0], Jwt.decode()[1]
#     return user


def id_generator(size=4, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def alpha_id_generator(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def modify_slz_error(errors):
    final_error = list()
    for key, value in errors.items():
        final_error.append(
            {'error': str(key) + ': ' + str(value[0])}
        )
    return final_error


def send_error(error, status=False, data=None):
    if data is None:
        data = {}
    return {'message': [{'error': error}], 'data': data, 'status': status}, HTTP_400_BAD_REQUEST


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.auth_type) + six.text_type(timestamp) +
                six.text_type(user.is_active) + six.text_type(user.email)
        )


account_activation_token = TokenGenerator()
