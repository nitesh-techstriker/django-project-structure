from rest_framework.views import APIView
from rest_framework.response import Response
from admin_inventory.services import *
from admin_inventory.selectors import *
from utils.common import get_input_data


class ProductView(APIView):
    """
    This is the Product Api View for Admin
    """

    @staticmethod
    def get(request):
        input_data = get_input_data(request)
        response = get_product(input_data)
        return Response(response)

    @staticmethod
    def post(request):
        input_data = get_input_data(request)
        response = create_product(input_data)
        return Response(response)

    @staticmethod
    def update(request):
        input_data = get_input_data(request)
        response = update_product(input_data)
        return Response(response)

    @staticmethod
    def delete(request):
        input_data = get_input_data(request)
        response = delete_product(input_data)
        return Response(response)


class CategoryView(APIView):
    """
    This is the Product Api View for Admin
    """

    @staticmethod
    def get(request):
        input_data = get_input_data(request)
        response = get_category(input_data)
        return Response(response)

    @staticmethod
    def post(request):
        input_data = get_input_data(request)
        response = create_category(input_data)
        return Response(response)

    @staticmethod
    def delete(request):
        input_data = get_input_data(request)
        response = delete_category(input_data)
        return Response(response)


class TagView(APIView):
    """
    This is the Product Api View for Admin
    """

    @staticmethod
    def get(request):
        input_data = get_input_data(request)
        response = get_tag(input_data)
        return Response(response)

    @staticmethod
    def post(request):
        input_data = get_input_data(request)
        response = create_tag(input_data)
        return Response(response)

    @staticmethod
    def delete(request):
        input_data = get_input_data(request)
        response = delete_tag(input_data)
        return Response(response)
