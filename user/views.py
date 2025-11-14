from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.shortcuts import get_object_or_404

from .models import Goal, Step, Attendance
from .serializers import GoalSerializer, StepSerializer, AttendanceSerializer

class UserGoalsView(APIView):
    def get(self, request, user_id):
        goals = Goal.objects.filter(user_id=user_id).order_by("-id")
        serializer = GoalSerializer(goals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateStepStatusView(APIView):
    def post(self, request):
        step_id = request.data.get("step_id")
        new_status = request.data.get("status")

        step = get_object_or_404(Step, id=step_id)
        step.status = new_status
        step.save()

        return Response({"message": "Step updated successfully"}, status=200)


class TodayAttendanceView(APIView):
    def get(self, request, user_id):
        today = timezone.now().date()
        attendance, created = Attendance.objects.get_or_create(
            user_id=user_id, date=today
        )
        serializer = AttendanceSerializer(attendance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CheckInView(APIView):
    def post(self, request, user_id):
        today = timezone.now().date()
        attendance, created = Attendance.objects.get_or_create(
            user_id=user_id, date=today
        )

        attendance.checkins += 1
        attendance.save()

        return Response(AttendanceSerializer(attendance).data, status=200)


class CheckOutView(APIView):
    def post(self, request, user_id):
        today = timezone.now().date()
        attendance, created = Attendance.objects.get_or_create(
            user_id=user_id, date=today
        )

        attendance.checkouts += 1
        
        # Example: Calculate hours (you can implement real time tracking)
        attendance.total_hours = attendance.checkins * 0.5  
        
        attendance.save()

        return Response(AttendanceSerializer(attendance).data, status=200)
