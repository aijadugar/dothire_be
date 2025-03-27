from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

@csrf_exempt  # Remove CSRF protection for testing (only for development)
def upload_resume(request):
    if request.method == 'POST' and request.FILES.get('resume'):
        resume = request.FILES['resume']  # Get uploaded file
        file_name = default_storage.save('resume/' + resume.name, resume)  # Save file

        return JsonResponse({"message": "Resume uploaded successfully!", "file": file_name})

    return JsonResponse({"error": "Invalid request"}, status=400)
