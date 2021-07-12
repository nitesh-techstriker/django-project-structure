from rest_framework.views import APIView
from rest_framework.response import Response
from builder.services.admin_builder import *
from builder.selectors.admin_builder import *
from utils.common import get_input_data


class ProductView(APIView):
    """
    This is the Product Api View for Admin
    """

    @staticmethod
    def get(request):
        input_data = get_input_data(request)
        response, status = get_product(input_data)
        return Response(response, status=status)

    @staticmethod
    def post(request):
        input_data = get_input_data(request)
        response, status = create_product(input_data)
        return Response(response, status=status)

    @staticmethod
    def update(request):
        input_data = get_input_data(request)
        response, status = update_product(input_data)
        return Response(response, status=status)

    @staticmethod
    def delete(request):
        input_data = get_input_data(request)
        response, status = delete_product(input_data)
        return Response(response, status=status)


class CategoryView(APIView):
    """
    This is the Product Api View for Admin
    """

    @staticmethod
    def get(request):
        input_data = get_input_data(request)
        response, status = get_category(input_data)
        return Response(response, status=status)

    @staticmethod
    def post(request):
        input_data = get_input_data(request)
        response, status = create_category(input_data)
        return Response(response, status=status)

    @staticmethod
    def delete(request):
        input_data = get_input_data(request)
        response, status = delete_category(input_data)
        return Response(response, status=status)


class TagView(APIView):
    """
    This is the Product Api View for Admin
    """

    @staticmethod
    def get(request):
        input_data = get_input_data(request)
        response, status = get_tag(input_data)
        return Response(response, status=status)

    @staticmethod
    def post(request):
        input_data = get_input_data(request)
        response, status = create_tag(input_data)
        return Response(response, status=status)

    @staticmethod
    def delete(request):
        input_data = get_input_data(request)
        response, status = delete_tag(input_data)
        return Response(response, status=status)
