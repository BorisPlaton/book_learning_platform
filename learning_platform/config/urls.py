from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

from courses.views import CourseListView


urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LoginView.as_view(), name='logout'),
    path('course/', include('courses.urls')),
    path('', CourseListView.as_view(), name='course_list'),
    path('admin/', admin.site.urls),
]
