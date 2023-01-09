
from django.shortcuts import Http404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets

# Create your views here.
from .serializers import ApiSerializer
from bug_page.models import BugDetail

class ApiViewSet(viewsets.ModelViewSet):
    queryset = BugDetail.objects.all()
    serializer_class = ApiSerializer


    @csrf_exempt
    def BugView(request, bug_id):
        try:
            bug = BugDetail.objects.get(bug_id=bug_id)

        except BugDetail.DoesNotExist:
            raise Http404('Not found')

        if request.method == 'GET':
            serializer = ApiSerializer(bug)
            return JsonResponse(serializer.data, status=200)
