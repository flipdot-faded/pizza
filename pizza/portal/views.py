from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import simplejson
from django.views.generic import TemplateView

from portal import forms

class PortalView(TemplateView):

    @property
    def ajax_template_name(self):
        first, sep, last = self.template_name.rpartition('/')
        return '/'.join([first, 'ajax', last])


class IndexView(PortalView):
    template_name = 'portal/index.html'


class LoginView(PortalView):
    template_name = 'portal/login.html'
    form_class = forms.LoginForm

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class()
        context['form'] = form
        if request.is_ajax():
            return render(self.request, self.ajax_template_name, context)
        return render(self.request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            data = {}
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    #login(request, user)
                    data['success'] = True
                else:
                    data['success'] = False
            else:
                data['success'] = False
            return HttpResponse(simplejson.dumps(data), content_type='application/json')
        return HttpResponse('some non ajax post')
