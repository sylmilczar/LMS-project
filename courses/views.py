from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import models


class CreateCourseView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Course
    fields = ('title', 'subject', 'slug', 'overview', 'course_image')
    template_name = 'courses/create_course.html'
    permission_required = 'courses.add_course'
    login_url = reverse_lazy('users:login')
    raise_exception = False
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CreateSubjectView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Subject
    fields = ('title', 'slug')
    template_name = 'courses/add_subject.html'
    permission_required = 'courses.add_subject'
    login_url = reverse_lazy('users:login')
    raise_exception = False
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
