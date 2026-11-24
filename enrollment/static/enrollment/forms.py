
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            'student_id',
            'full_name',
            'email',
            'contact_number',
            'address',
            'date_of_birth',
            'gender',
            'course',
            'year_level',
            'section',
            'enrollment_status',
            'guardian_name',
            'guardian_contact',
            'previous_school',
        ]

        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'address': forms.Textarea(
                attrs={'rows': 3}
            ),
        }
