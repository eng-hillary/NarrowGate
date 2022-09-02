from django.urls import URLPattern, path
from . import views

app_name = 'common'

urlpatterns = [
    path('', views.SubjectListView.as_view(), name='subjects-list'),
    path('create/', views.SubjectCreateView.as_view(), name='subject-create'),
    # path('detail/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    # path('update/<int:pk>/', views.StudentUpdateView.as_view(), name='student-update'),
    # path('delete/<int:pk>/', views.StudentDeleteView.as_view(), name='student-delete'),
] 