from django.urls import URLPattern, path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.StudentListView.as_view(), name='students-list'),
    path('create/', views.StudentCreateView.as_view(), name='student-create'),
    path('detail/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    path('update/<int:pk>/', views.StudentUpdateView.as_view(), name='student-update'),
    path('delete/<int:pk>/', views.StudentDeleteView.as_view(), name='student-delete'),
    path('profile/<int:pk>/', views.StudentProfileView.as_view(), name='student-profile'),
] 