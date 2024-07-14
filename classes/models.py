from django.db import models

# Create your models here.
class Class(models.Model):
    class_id = models.PositiveSmallIntegerField()
    class_name = models.CharField(max_length = 20)
    teacher= models.CharField(max_length = 20)
    meeting_days = models.DateField()
    academic_year = models.DateField()
    class_status = models.CharField(max_length = 30)
    class_capacity = models.PositiveSmallIntegerField()
    general_performance = models.CharField(max_length = 15)

    def __str__(self):
        return f"{self.class_name} {self.class_id}"


class ClassPeriod(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.CharField(max_length = 20)
    classroom = models.CharField(max_length = 20)
    date_of_the_week = models.DateField()

    def __str__(self):
        return f"{self.start_time} {self.end_time}"