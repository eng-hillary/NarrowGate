from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from . models import Subject
from . forms import SubjectForm

class SubjectListView(LoginRequiredMixin,ListView):
    model = Subject
    template_name = 'common/subjects_list.html'
    context_object_name = 'subjects'

class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    # form_class = SubjectForm
    fields = ['code', 'name', 'class_taught']
    template_name = 'common/subject_create.html'
    success_url = reverse_lazy('common:subjects-list')

