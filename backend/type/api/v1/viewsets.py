from rest_framework import authentication
from type.models import Type
from .serializers import TypeSerializer
from rest_framework import viewsets


class TypeViewSet(viewsets.ModelViewSet):
    serializer_class = TypeSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Type.objects.all()
