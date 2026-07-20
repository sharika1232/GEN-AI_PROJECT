from django import forms
from .models import Resume


class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume

        fields = [
            "title",
            "resume_file",
            "company_name",
            "job_role",
            "job_description",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Resume Title",
                }
            ),

            "resume_file": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": ".pdf,.doc,.docx",
                }
            ),

            "job_description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 10,
                    "placeholder": """Paste the complete Job Description here...

Example:

Python Developer

Required Skills:
Python
Django
REST API
Docker
AWS
Git
SQL
""",
                }
            ),

        }