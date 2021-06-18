from admin_inventory.models import *
from admin_inventory.serializers import *
from utils.common import *
from rest_framework.status import *
from utils.constants import *


def create_product(input_data):
    error = product_create_validations(input_data)
    if error:
        return generate_response(message=error, status=HTTP_400_BAD_REQUEST)
    serializer = ProductSerializer(data=input_data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    else:
        return generate_response(message=serializer.error_messages, status=HTTP_400_BAD_REQUEST)
    return generate_response(message='Success! Product added.', status=HTTP_201_CREATED)


def product_create_validations(input_data):
    error = None
    if 'type' not in input_data or not input_data['type'] or input_data['type'] not in DEFAULT_PRODUCT_TYPE:
        error = 'Error! type is missing or invalid, type should be one of ' + DEFAULT_PRODUCT_TYPE.join(',')
    elif 'product_translation' not in input_data or not input_data['product_translation']:
        error = 'Error! product_translation is missing or invalid.'
    elif 'product_translation' in input_data:
        if 'language' not in input_data['product_translation'] or not input_data['product_translation']['language']:
            error = 'Error! language is missing or invalid in product_translation.'
        elif 'title' not in input_data['product_translation'] or not input_data['product_translation']['title']:
            error = 'Error! title is missing or invalid in product_translation.'
        elif 'description' not in input_data['product_translation']:
            error = 'Error! description is missing or invalid in product_translation.'

    return error


def update_product(input_data):
    if 'id' not in input_data or not input_data['id']:
        return generate_response(message='Error! id is missing or invalid.', status=HTTP_400_BAD_REQUEST)
    if 'language' not in input_data or not input_data['language']:
        return generate_response(message='Error! language is missing or invalid.', status=HTTP_400_BAD_REQUEST)
    product = AdminProductModel.objects.get(id=input_data['id'])
    if 'data' in input_data:
        product.data = input_data['data']
    if 'images' in input_data:
        product.images = input_data['images']
    if 'docs' in input_data:
        product.docs = input_data['docs']
    if 'is_premium' in input_data:
        product.is_premium = input_data['is_premium']
    if 'is_published' in input_data:
        product.is_published = input_data['is_published']
    if 'link' in input_data:
        product.link = input_data['link']
    if 'author' in input_data:
        product.author = input_data['author']
    if 'meta' in input_data:
        product.meta = input_data['meta']
    if 'time' in input_data:
        product.time = input_data['time']
    if 'product_translation' in input_data:
        update_product_translation(input_data)
    product.save()
    return generate_response(data=product, message='Success! updated.')


def update_product_translation(product, input_data):
    product_translation = AdminProductTranslationModel.objects.get(product=product.id)
    if product_translation.language != input_data['language']:
        product_translation = AdminProductTranslationModel(product=product, language=input_data['language'])
    if 'title' in input_data:
        product_translation.title = input_data['title']
    if 'description' in input_data:
        product_translation.description = input_data['description']
    product_translation.save()


def update_service(product, input_data):
    if product.type == SERVICE_TYPE:
        service = AdminServiceModel.objects.get(product=product.id)
        if 'service_type' in input_data:
            service.service_type = input_data['service_type']
        if 'entry_name' in input_data:
            service.entry_name = input_data['entry_name']
        service.save()


def delete_product(input_data):
    if 'id' not in input_data or not input_data['id']:
        return generate_response(message='Error! id is missing or invalid.', status=HTTP_400_BAD_REQUEST)
    AdminProductModel.objects.filter(id=input_data['id']).update(is_deleted=True)
    return generate_response(message='Success! product deleted.')
