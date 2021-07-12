import uuid
import requests
import string
import random
from django.core.files.storage import FileSystemStorage
import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.status import *


# import pandas as pd

def get_input_data(request):
    if request.method == 'GET':
        input_data = request.GET
    else:
        input_data = request.data
    return input_data


def generate_response(data=None, message=None, status=200):
    if status == HTTP_200_OK or status == HTTP_201_CREATED:
        status_bool = True
    else:
        status_bool = False

    return {
               'data': data,
               'message': modify_slz_error(message, status_bool),
               'status': status_bool,
           }, status


def modify_slz_error(message, status):
    final_error = list()
    if message:
        if type(message) == str:
            if not status:
                final_error.append(
                    {
                        'error': message
                    }
                )
            else:
                final_error = message
        elif type(message) == list:
            final_error = message
        else:
            for key, value in message.items():
                final_error.append(
                    {'error': str(key) + ': ' + str(value[0])}
                )
    else:
        final_error = None
    return final_error


def send_error(error, status=False, data=None):
    if data is None:
        data = {}
    return {'message': [{'error': error}], 'data': data, 'status': status}, 400


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


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.auth_type) + six.text_type(timestamp) +
                six.text_type(user.is_active) + six.text_type(user.email)
        )


account_activation_token = TokenGenerator()
