from django.urls import path
from .views import UserGoalsView, TodayAttendanceView, CheckInView, CheckOutView, UpdateStepStatusView

urlpatterns = [

    # Goals
    path("goals/<int:user_id>/", UserGoalsView.as_view(), name="user-goals"),
    path("update-step/", UpdateStepStatusView.as_view(), name="update-step"),

    # Attendance
    path("attendance/today/<int:user_id>/", TodayAttendanceView.as_view(), name="attendance-today"),
    path("attendance/check-in/<int:user_id>/", CheckInView.as_view(), name="check-in"),
    path("attendance/check-out/<int:user_id>/", CheckOutView.as_view(), name="check-out"),
]