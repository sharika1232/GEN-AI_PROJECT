from django.urls import path
from . import views


urlpatterns = [

    path(
        "upload/",
        views.upload_resume,
        name="upload_resume"
    ),

    path(
        "history/",
        views.resume_history,
        name="resume_history"
    ),

    path(
        "detail/<int:id>/",
        views.resume_detail,
        name="resume_detail"
    ),

    path(
        "download/<int:id>/",
        views.download_report,
        name="download_report"
    ),

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "compare/",
        views.compare_resumes,
        name="compare_resumes"
    ),

    path(
        "ranking/",
        views.resume_ranking,
        name="resume_ranking"
    ),

    path(
        "job-match/<int:id>/",
        views.job_match,
        name="job_match"
    ),

    path(
        "compare-versions/<int:old_id>/<int:new_id>/",
        views.compare_resume_versions,
        name="compare_resume_versions"
    ),

    # AI Cover Letter PDF Download
    path(
        "resume/<int:id>/download-cover-letter/",
        views.download_cover_letter,
        name="download_cover_letter"
    ),
    path(
        "chat/<int:id>/",
        views.chat_resume,
        name="chat_resume",
    ),

]