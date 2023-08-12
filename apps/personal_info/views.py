from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class TestView(APIView):

    def post(self, request, *args, **kwargs):
        print(self.request.body)
        response_text = 'Ohio'
        return Response(response_text, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        return Response('Works', status=status.HTTP_200_OK)
