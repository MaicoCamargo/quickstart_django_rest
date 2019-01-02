from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from snippets.models import Snippet
from snippets.serializers import UserSerializer, GroupSerializer, SnippetSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@csrf_exempt
def user_detail(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        query = User.objects.filter(id(1))
        print(query)
        user_serializer = UserSerializer(query, many=True)
        return JsonResponse(user_serializer.data, safe=False)

