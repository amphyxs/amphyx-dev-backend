from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework import status


class TestView(ListCreateAPIView):

    def post(self, request, *args, **kwargs):
        print(self.request.body)
        return Response('WTF', status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        return Response('Works', status=status.HTTP_200_OK)
