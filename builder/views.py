from rest_framework.views import APIView
from rest_framework.response import Response
from builder.services import *
from builder.selectors import *
from utils.common import get_input_data


class BuilderView(APIView):
    """
    This is the Builder Api View for User
    """

    @staticmethod
    def get(request):
        input_data = get_input_data(request)
        response, status = get_builder(input_data)
        return Response(response, status=status)

    @staticmethod
    def post(request):
        input_data = get_input_data(request)
        response, status = create_builder(input_data)
        return Response(response, status=status)

    @staticmethod
    def put(request):
        input_data = get_input_data(request)
        response, status = update_builder(input_data)
        return Response(response, status=status)

    @staticmethod
    def delete(request):
        input_data = get_input_data(request)
        response, status = delete_builder(input_data)
        return Response(response, status=status)
