from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Resume
from .serializers import ResumeSerializer
from .nlp_resume import extract_text, extract_resume_info
from .ml_ranking import rank_candidates
from .bias_detection import detect_bias

@api_view(['POST'])
def upload_resume(request):
    file = request.FILES['resume']
    text = extract_text(file.temporary_file_path())
    info = extract_resume_info(text)
    resume = Resume.objects.create(**info)
    return Response({"message": "Resume Uploaded", "data": ResumeSerializer(resume).data})

@api_view(['GET'])
def get_ranked_resumes(request, job_desc):
    resumes = Resume.objects.all()
    resume_texts = [r.experience + " " + r.skills for r in resumes]
    rankings = rank_candidates(resume_texts, job_desc)
    
    for i, (index, score) in enumerate(rankings):
        resumes[index].job_match_score = score
        resumes[index].save()

    return Response({"ranked_resumes": ResumeSerializer(resumes, many=True).data})
