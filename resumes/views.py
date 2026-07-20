from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Avg, Max, Min, Q
from reportlab.pdfgen import canvas
import json

from .forms import ResumeForm
from .models import Resume

from .utils import extract_resume_text
from .skills import extract_skills
from .ats import calculate_ats_score
from .career import recommend_jobs
from .suggestions import generate_suggestions
from .feedback import generate_feedback
from .cover_letter import generate_cover_letter
from .name_extractor import extract_candidate_name
from .interview import generate_interview_questions
from .ranking import rank_resumes
from .similarity import calculate_similarity
from .strength import calculate_strength
from .completeness import calculate_completeness
from .resume_improver import improve_resume
from .career_roadmap import generate_career_roadmap
from .score_breakdown import generate_score_breakdown
from .learning_resources import get_learning_resources
from .chatbot import get_chatbot_response
from .job_match import predict_job_match
from .version_compare import compare_versions
from .keyword_optimizer import optimize_keywords



# ==========================================================
# Upload Resume
# ==========================================================

@login_required
def upload_resume(request):

    if request.method == "POST":

        form = ResumeForm(request.POST, request.FILES)

        if form.is_valid():

            # Save Resume
            resume = form.save(commit=False)

            resume.user = request.user


            # New Cover Letter Details
            resume.company_name = request.POST.get(
                "company_name"
            )

            resume.job_role = request.POST.get(
                "job_role"
            )


            # Resume Version Handling
            latest_resume = Resume.objects.filter(
                user=request.user
            ).order_by(
                "-uploaded_at"
            ).first()


            if latest_resume:

                resume.version = latest_resume.version + 1
                resume.parent_resume = latest_resume

            else:

                resume.version = 1
                resume.parent_resume = None



            resume.save()



            # Extract Resume Text
            text = extract_resume_text(
                resume.resume_file.path
            )


            candidate_name = extract_candidate_name(
                text
            )


            resume.extracted_text = text
            resume.candidate_name = candidate_name



            # Extract Skills

            resume_skills = extract_skills(
                text
            )


            resume.skills = ", ".join(
                resume_skills
            )


            resume.save()



            # Job Description Skills

            job_description = resume.job_description


            job_skills = extract_skills(
                job_description
            )



            # ATS Score

            ats_result = calculate_ats_score(
                resume_skills,
                job_skills
            )



            # Similarity

            similarity = calculate_similarity(
                text,
                job_description
            )



            resume.ats_score = ats_result["score"]

            resume.save()



            # Recommendations

            recommended_jobs = recommend_jobs(
                resume_skills
            )


            suggestions = generate_suggestions(
                ats_result["missing_skills"]
            )


            resume_improvements = improve_resume(
                ats_result["missing_skills"],
                ats_result["score"]
            )



            # Completeness

            completeness_score, completeness_report = calculate_completeness(
                text
            )



            # Strength

            strength = calculate_strength(
                ats_result["score"],
                completeness_score
            )



            # Feedback

            feedback = generate_feedback(
                ats_result["score"],
                ats_result["matched_skills"],
                ats_result["missing_skills"],
            )



            # ================================
            # AI Cover Letter
            # ================================

            cover_letter = generate_cover_letter(
                candidate_name,
                resume.job_role,
                resume_skills,
                resume.company_name,
                resume.job_description,
            )


            # Save Cover Letter

            resume.cover_letter = cover_letter
            resume.save()



            # Interview Questions

            interview_questions = generate_interview_questions(
                resume_skills
            )



            return render(
                request,
                "resumes/result.html",
                {
                    "resume": resume,
                    "skills": resume_skills,
                    "job_skills": job_skills,
                    "ats_score": ats_result["score"],
                    "matched_skills": ats_result["matched_skills"],
                    "missing_skills": ats_result["missing_skills"],
                    "recommended_jobs": recommended_jobs,
                    "suggestions": suggestions,
                    "feedback": feedback,
                    "cover_letter": cover_letter,
                    "interview_questions": interview_questions,
                    "similarity": similarity,
                    "completeness_score": completeness_score,
                    "completeness_report": completeness_report,
                    "strength": strength,
                    "resume_improvements": resume_improvements,
                },
            )


    else:

        form = ResumeForm()



    return render(
        request,
        "resumes/upload_resume.html",
        {
            "form": form,
        },
    )


# ==========================================================
# Resume History
# ==========================================================

@login_required
def resume_history(request):

    resumes = Resume.objects.filter(
        user=request.user
    ).order_by("-uploaded_at")

    return render(
        request,
        "resumes/history.html",
        {
            "resumes": resumes,
        },
    )

# ==========================================================
# Resume Detail
# ==========================================================

@login_required
def resume_detail(request, id):

    resume = Resume.objects.get(
        id=id,
        user=request.user
    )

    improvement_suggestions = []

    if not resume.extracted_text:
        improvement_suggestions.append(
            "Resume text extraction failed. Please upload again."
        )

    if "projects" not in resume.extracted_text.lower():
        improvement_suggestions.append(
            "Add more project details with technologies used and outcomes."
        )

    if "github" not in resume.extracted_text.lower():
        improvement_suggestions.append(
            "Add your GitHub profile link to showcase your coding projects."
        )

    if "linkedin" not in resume.extracted_text.lower():
        improvement_suggestions.append(
            "Add your LinkedIn profile link for better recruiter visibility."
        )

    if len(resume.extracted_text.split()) < 300:
        improvement_suggestions.append(
            "Resume content is short. Add more details about your experience and achievements."
        )

    if not improvement_suggestions:
        improvement_suggestions.append(
            "Your resume is already strong. Keep updating skills and projects regularly."
        )

    # Resume Skills
    resume_skills = (
        resume.skills.split(", ")
        if resume.skills
        else []
    )

    # Job Skills
    job_skills = extract_skills(
        resume.job_description
    )

    # ATS Score
    ats_result = calculate_ats_score(
        resume_skills,
        job_skills
    )

    # Similarity
    similarity = calculate_similarity(
        resume.extracted_text,
        resume.job_description
    )

    # Recommended Jobs
    recommended_jobs = recommend_jobs(
        resume_skills
    )

    # Keyword Optimization
    keyword_report = optimize_keywords(
        resume_skills,
        "Python Developer"
    )

    # Career Roadmap
    career_roadmap = generate_career_roadmap(
        resume_skills
    )

    # Interview Questions
    interview_questions = generate_interview_questions(
        resume_skills
    )

    # Suggestions
    suggestions = generate_suggestions(
        ats_result["missing_skills"]
    )

    # Resume Improvements
    resume_improvements = improve_resume(
        ats_result["missing_skills"],
        resume.ats_score
    )

    # Completeness
    completeness_score, completeness_report = calculate_completeness(
        resume.extracted_text
    )

    # Strength
    strength = calculate_strength(
        resume.ats_score,
        completeness_score
    )

    # Score Breakdown
    score_breakdown = generate_score_breakdown(
        resume.ats_score,
        completeness_score
    )

    # Learning Resources
    learning_resources = get_learning_resources(
        resume_skills
    )

    # Feedback
    feedback = generate_feedback(
        resume.ats_score,
        ats_result["matched_skills"],
        ats_result["missing_skills"],
    )

    # Candidate Name
    candidate_name = extract_candidate_name(
        resume.extracted_text
    )

    # AI Cover Letter
    cover_letter = generate_cover_letter(
        candidate_name=candidate_name,
        job_role=resume.job_role or "Software Developer",
        skills=resume_skills,
        company_name=resume.company_name or "Your Company",
        job_description=resume.job_description or "",
    )

    # Save Cover Letter
    resume.cover_letter = cover_letter
    resume.save(update_fields=["cover_letter"])

    return render(
        request,
        "resumes/detail.html",
        {
            "resume": resume,
            "skills": resume_skills,
            "job_skills": job_skills,
            "ats_score": resume.ats_score,
            "matched_skills": ats_result["matched_skills"],
            "missing_skills": ats_result["missing_skills"],
            "recommended_jobs": recommended_jobs,
            "suggestions": suggestions,
            "feedback": feedback,
            "cover_letter": cover_letter,
            "similarity": similarity,
            "completeness_score": completeness_score,
            "completeness_report": completeness_report,
            "strength": strength,
            "resume_improvements": resume_improvements,
            "improvement_suggestions": improvement_suggestions,
            "career_roadmap": career_roadmap,
            "interview_questions": interview_questions,
            "score_breakdown": score_breakdown,
            "learning_resources": learning_resources,
            "keyword_report": keyword_report,
        },
    )
 

# ==========================================================
# Download PDF Report
# ==========================================================

@login_required
def download_report(request, id):

    resume = Resume.objects.get(
        id=id,
        user=request.user
    )

    response = HttpResponse(
        content_type="application/pdf"
    )

    response["Content-Disposition"] = (
        f'attachment; filename="{resume.title}_report.pdf"'
    )

    pdf = canvas.Canvas(response)

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(
        50,
        800,
        "AI Resume Screener Report"
    )

    pdf.setFont("Helvetica", 12)

    y = 760

    lines = [
        f"Resume Title: {resume.title}",
        f"ATS Score: {resume.ats_score}%",
        "",
        "Skills:",
        resume.skills,
        "",
        "Job Description:",
        resume.job_description,
    ]

    for line in lines:

        pdf.drawString(
            50,
            y,
            str(line)[:90]
        )

        y -= 25

    pdf.save()

    return response


# ==========================================================
# Dashboard
# ==========================================================

@login_required
def dashboard(request):

    resumes = Resume.objects.filter(
        user=request.user
    ).order_by("-uploaded_at")

    total_resumes = resumes.count()

    average_score = resumes.aggregate(
        Avg("ats_score")
    )["ats_score__avg"] or 0

    highest_score = resumes.aggregate(
        Max("ats_score")
    )["ats_score__max"] or 0

    lowest_score = resumes.aggregate(
        Min("ats_score")
    )["ats_score__min"] or 0

    latest_resume = resumes.first()

    best_resume = resumes.order_by(
        "-ats_score"
    ).first()

    chart_labels = []
    chart_scores = []

    for resume in resumes:
        chart_labels.append(resume.title)
        chart_scores.append(resume.ats_score)

    context = {

        "total_resumes": total_resumes,

        "average_score": round(average_score),

        "highest_score": highest_score,

        "lowest_score": lowest_score,

        "latest_resume": latest_resume,

        "best_resume": best_resume,

        "resumes": resumes,

        "chart_labels": json.dumps(chart_labels),

        "chart_scores": json.dumps(chart_scores),

    }

    return render(
        request,
        "resumes/dashboard.html",
        context,
    )


# ==========================================================
# Compare Resumes
# ==========================================================

@login_required
def compare_resumes(request):

    resumes = Resume.objects.filter(
        user=request.user
    ).order_by("-uploaded_at")

    resume1 = None
    resume2 = None

    if request.method == "POST":

        resume1 = Resume.objects.get(
            id=request.POST["resume1"],
            user=request.user,
        )

        resume2 = Resume.objects.get(
            id=request.POST["resume2"],
            user=request.user,
        )

    return render(
        request,
        "resumes/compare.html",
        {
            "resumes": resumes,
            "resume1": resume1,
            "resume2": resume2,
        },
    )

# ---------------------------------------------
# Resume Ranking
# ---------------------------------------------

@login_required
def resume_ranking(request):

    resumes = Resume.objects.filter(
        user=request.user
    )

    ranked_resumes = rank_resumes(resumes)

    return render(
        request,
        "resumes/ranking.html",
        {
            "ranked_resumes": ranked_resumes,
        },
    )


# ==========================================================
# AI Job Match Predictor
# ==========================================================

@login_required
def job_match(request, id):

    resume = get_object_or_404(
        Resume,
        id=id,
        user=request.user
    )

    result = None
    job_description = ""


    if request.method == "POST":


        job_description = request.POST.get(
            "job_description",
            ""
        ).strip()



        if job_description:


            result = predict_job_match(

                resume.extracted_text,

                job_description

            )


        else:


            result = {

                "error":
                "Please enter a job description."

            }



    return render(

        request,

        "resumes/job_match.html",

        {

            "resume": resume,

            "result": result,

            "job_description": job_description,

        },

    )

@login_required
def compare_resume_versions(request, old_id, new_id):

    old_resume = Resume.objects.get(
        id=old_id,
        user=request.user
    )

    new_resume = Resume.objects.get(
        id=new_id,
        user=request.user
    )

    comparison = compare_versions(
        old_resume,
        new_resume
    )

    return render(
        request,
        "resumes/version_compare.html",
        {
            "old_resume": old_resume,
            "new_resume": new_resume,
            "comparison": comparison,
        },
    )

# ==========================================================
# Compare Resume Versions
# ==========================================================

@login_required
def compare_resume_versions(request, old_id, new_id):

    old_resume = Resume.objects.get(
        id=old_id,
        user=request.user
    )

    new_resume = Resume.objects.get(
        id=new_id,
        user=request.user
    )

    comparison = compare_versions(
        old_resume,
        new_resume
    )

    return render(
        request,
        "resumes/version_compare.html",
        {
            "old_resume": old_resume,
            "new_resume": new_resume,
            "comparison": comparison,
        },
    )

# ==========================================================
# Download AI Cover Letter PDF
# ==========================================================

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from io import BytesIO
from reportlab.pdfgen import canvas


@login_required
def download_cover_letter(request, id):

    resume = Resume.objects.get(
        id=id,
        user=request.user
    )

    cover_letter = resume.cover_letter or "No cover letter available."


    buffer = BytesIO()

    pdf = canvas.Canvas(buffer)

    pdf.setTitle("AI Cover Letter")


    text = pdf.beginText(
        50,
        800
    )

    text.setFont(
        "Helvetica",
        12
    )


    for line in cover_letter.split("\n"):

        text.textLine(line)


    pdf.drawText(text)

    pdf.save()


    buffer.seek(0)


    response = HttpResponse(
        buffer,
        content_type="application/pdf"
    )


    response["Content-Disposition"] = (
        'attachment; filename="AI_Cover_Letter.pdf"'
    )


    return response

from django.shortcuts import get_object_or_404

@login_required
def chat_resume(request, id):

    resume = get_object_or_404(
        Resume,
        id=id,
        user=request.user
    )

    answer = ""
    question = ""


    if request.method == "POST":


        question = request.POST.get(
            "question",
            ""
        )


        print("\n==============================")
        print("CHATBOT VIEW STARTED")
        print("QUESTION FROM USER :", question)
        print("==============================")


        try:

            answer = get_chatbot_response(
                question,
                resume
            )


            print("AI RESPONSE GENERATED:")
            print(answer)
            print("==============================\n")


        except Exception as e:


            print("==============================")
            print("CHATBOT ERROR:")
            print(e)
            print("==============================\n")


            answer = (
                "Sorry, something went wrong while generating response."
            )


    return render(
        request,
        "resumes/chatbot.html",
        {
            "resume": resume,
            "answer": answer,
            "question": question,
        }
    )