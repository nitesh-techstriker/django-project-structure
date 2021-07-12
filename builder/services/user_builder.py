from builder.models.user_builder import *
from builder.serializers.user_builder import *
from utils.common import *
from rest_framework.status import *
from utils.constants import *
from builder.models.admin_builder import AdminProductModel, AdminProductTranslationModel

category_types = [RESUME_TYPE, SERVICE_TYPE, BOOK_TYPE, PITCH_TYPE, PODCAST_TYPE, VIDEO_TYPE, ADVICE_TYPE,
                  ADVICE_TYPE]


def create_builder(input_data):
    error = validate_builder(input_data)
    if error:
        return error
    if 'product_id' in input_data or input_data['product_id']:
        error = validate_payment(input_data)
        input_data = create_admin_to_builder_data(input_data)
    serializer = BuilderSerializer(data=input_data)
    if serializer.is_valid():
        builder = serializer.save()
        input_data['id'] = builder.id
    else:
        return generate_response(message=serializer.errors, status=HTTP_400_BAD_REQUEST)
    return generate_response(data=input_data, message='Success! added.', status=HTTP_201_CREATED)


def validate_payment(input_data):
    return True


def create_admin_to_builder_data(input_data):
    product = AdminProductTranslationModel.objects.filter(product_id=input_data['product_id']).values(

    )


def update_builder(input_data):
    if 'id' not in input_data or not input_data['id']:
        return generate_response(message='Error! id is missing or invalid.', status=HTTP_400_BAD_REQUEST)
    builder = BuilderModel.objects.get(id=input_data['id'])
    if 'title' in input_data:
        builder.title = input_data['title']
    if 'description' in input_data:
        builder.description = input_data['description']
    if 'data' in input_data:
        builder.data = input_data['data']
    if 'images' in input_data:
        builder.images = input_data['images']
    if 'docs' in input_data:
        builder.docs = input_data['docs']
    builder.save()
    return generate_response(data=input_data, message='Success! updated.', status=HTTP_201_CREATED)


def delete_builder(input_data):
    if 'id' not in input_data or not input_data['id']:
        return generate_response(message='Error! id is missing or invalid.', status=HTTP_400_BAD_REQUEST)
    BuilderModel.objects.filter(id=input_data['id']).delete()
    return generate_response(message='Success! deleted.')


def validate_builder(input_data):
    if 'type' not in input_data or not input_data['type'] or input_data['type'] not in category_types:
        return generate_response(
            message=f'Error! type is missing or invalid. it should be one of {", ".join(category_types)}')
    elif 'title' not in input_data or not input_data['title']:
        return generate_response(message='Error! title is missing or invalid.', status=HTTP_400_BAD_REQUEST)
    elif 'language' not in input_data or not input_data['language']:
        return generate_response(message='Error! language is required.', status=HTTP_400_BAD_REQUEST)
    elif 'user' not in input_data or not input_data['user']:
        return generate_response(message='Error! user is missing or invalid.', status=HTTP_400_BAD_REQUEST)
    else:
        return None
