from django.db import models

class Student(models.Model):
    YEAR_LEVEL_CHOICES = [
        ('1st Year', '1st Year'),
        ('2nd Year', '2nd Year'),
        ('3rd Year', '3rd Year'),
        ('4th Year', '4th Year'),
    ]

    STATUS_CHOICES = [
        ('Enrolled', 'Enrolled'),
        ('Pending', 'Pending'),
        ('Dropped', 'Dropped'),
    ]

    # Personal Info
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    # Academic / Enrollment Info
    course = models.CharField(max_length=100)
    year_level = models.CharField(max_length=20, choices=YEAR_LEVEL_CHOICES)
    section = models.CharField(max_length=50)
    enrollment_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Enrolled')
    date_enrolled = models.DateField(auto_now_add=True)

    # Background Info
    previous_school = models.CharField(max_length=150)
    guardian_name = models.CharField(max_length=150)
    guardian_contact = models.CharField(max_length=20)
    medical_notes = models.TextField(blank=True, default="None")

    def __str__(self):
        return f"{self.student_id} - {self.last_name}, {self.first_name}"