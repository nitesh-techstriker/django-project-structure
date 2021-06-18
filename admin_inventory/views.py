from rest_framework.views import APIView
from rest_framework.response import Response
from admin_inventory.utils.services import *
from admin_inventory.utils.selectors import *
from utils.common import get_input_data
from .serializers import *


class ProductView(APIView):
    """
    This is the Product Api View for Admin
    """

    def get(self, request):
        input_data = get_input_data(request)
        response, status = get_product(input_data)
        return Response(response, status=status)

    def post(self, request):
        input_data = get_input_data(request)
        response, status = create_product(input_data)
        return Response(response, status=status)

    def update(self, request):
        input_data = get_input_data(request)
        response, status = update_product(input_data)
        return Response(response, status=status)

    def delete(self, request):
        input_data = get_input_data(request)
        response, status = delete_product(input_data)
        return Response(response, status=status)
