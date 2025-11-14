from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class Role(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    USER = "USER", "User"

class User(AbstractUser):
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.USER)

    def __str__(self):
        return self.username

class GoalType(models.TextChoices):
    TASK = "task", "Task"
    GOAL = "goal", "Goal"

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="goals")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=10, choices=GoalType.choices, default=GoalType.GOAL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class StepStatus(models.TextChoices):
    BACKLOG = "backlog", "Backlog"
    IN_PROGRESS = "in_progress", "In Progress"
    COMPLETED = "completed", "Completed"

class Step(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name="steps")
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=StepStatus.choices, default=StepStatus.BACKLOG)

    def __str__(self):
        return f"{self.goal.title} → {self.title}"




class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="attendance")
    date = models.DateField(default=timezone.now)
    checkins = models.IntegerField(default=0)
    checkouts = models.IntegerField(default=0)
    total_hours = models.FloatField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.date}"
