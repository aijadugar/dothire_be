from django.urls import path
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .views import upload_resume

@api_view(['GET'])
def api_root(request):
    return Response({
        "upload_resume": request.build_absolute_uri('upload-resume/')
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('upload-resume/', upload_resume, name='upload-resume'),
]
