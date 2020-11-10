from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def list(self, request):
        pass

    def create(self, request):
        return Response({"detail": "Method \"POST\" not allowed."}, status=405)

    def retrieve(self, request, pk=None):
        pass


