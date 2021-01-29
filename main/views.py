# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView

from .mixins import AjaxTemplateMixin


class About(TemplateView):
    template_name = 'main/about.html'


class Index(TemplateView):
    template_name = 'main/index.html'


class CustomLoginView(AjaxTemplateMixin, LoginView):
    template_name = 'account/modal_login.html'
    form_class = AuthenticationForm
