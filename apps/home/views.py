from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework import status


class TestView(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        return Response('Works', status=status.HTTP_200_OK)
