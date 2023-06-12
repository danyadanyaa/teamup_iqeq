from datetime import datetime
from string import ascii_letters
from random import choice

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from api.models import Test
from api.serializers import TestSerializer, IqSerializer, EqSerializer, ResultSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.order_by("id")
    serializer_class = TestSerializer
    http_method_names = ['get', 'post']

    def get_serializer_class(self):
        if self.request.path == '/api/tests/iq/':
            return IqSerializer
        elif self.request.path == '/api/tests/iq/':
            return EqSerializer
        elif self.request.path == '/api/tests/result/':
            return ResultSerializer
        else:
            return self.serializer_class

    @action(detail=False, methods=['get'], url_path='login')
    def login(self, request):
        unique = ''.join(choice(ascii_letters) for _ in range(10))
        while Test.objects.filter(login=unique).exists():
            unique = ''.join(choice(ascii_letters) for _ in range(10))
        created_login = Test.objects.create(login=unique)
        return Response({'login': created_login.login}, status=HTTP_201_CREATED)

    @action(detail=False, methods=['post'], url_path='iq')
    def iq(self, request):
        test = get_object_or_404(Test, login=request.data['login'])
        serializer = IqSerializer(test, data=request.data)
        serializer.is_valid()
        test.iq_points, test.iq_time = request.data['iq_points'], datetime.utcnow()
        test.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

    @action(detail=False, methods=['post'], url_path='eq')
    def eq(self, request):
        test = get_object_or_404(Test, login=request.data['login'])
        serializer = EqSerializer(test, data=request.data)
        serializer.is_valid()
        test.eq_result, test.eq_time = request.data['eq_result'], datetime.utcnow()
        test.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

    @action(detail=False, methods=['post'], url_path='result')
    def result(self, request):
        test = get_object_or_404(Test, login=request.data['login'])
        serializer = ResultSerializer(test, data=request.data)
        serializer.is_valid()
        return Response(serializer.data, status=HTTP_201_CREATED)
