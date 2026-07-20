from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=200
    )

    resume_file = models.FileField(
        upload_to="resumes/"
    )

    extracted_text = models.TextField(
        blank=True
    )

    skills = models.TextField(
        blank=True
    )

    job_description = models.TextField(
        blank=True
    )

    job_role = models.CharField(
    max_length=200,
    blank=True,
    null=True
)

    company_name = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    ats_score = models.IntegerField(
        default=0
    )


    # AI Generated Cover Letter

    cover_letter = models.TextField(
        blank=True,
        null=True
    )


    # Resume Version Tracking

    version = models.IntegerField(
        default=1
    )

    parent_resume = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="versions"
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.title