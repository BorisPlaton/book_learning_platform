from django.urls import path
from django.views.decorators.cache import cache_page

from students import views


app_name = 'students'

urlpatterns = [
    path('register/', views.StudentRegistrationView.as_view(), name='student_registration'),
    path('enroll-course/', views.StudentEnrollView.as_view(), name='student_enroll_course'),
    path('course/', views.StudentEnrollView.as_view(), name='student_course_list'),
    path('course/<int:pk>/', cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
         name='student_course_detail'),
    path('course/<int:pk>/<int:module_id>/', cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
         name='student_course_detail_module'),
]
