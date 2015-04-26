from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext,loader
from .models import Entry
from .forms import EntryCreateForm
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
import datetime
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from django.contrib import auth
from django.core.context_processors import csrf

def custom_login(request, *args, **kwargs):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html',c)

def auth_view(request):
    username = request.POST.get('username' , '')
    password = request.POST.get('password' , '')
    user= auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect("loggedin/")
    else:
        return HttpResponseRedirect("login/")

def loggedin(request):

    return render_to_response('loggedin.html',{'full_name' : request.user.username})

def custom_logout(request):
    return render_to_response('loggedout.html')


class EntryFormView(ListView):
    form_class= EntryCreateForm
    initial= { 'key': 'value'}
    template_name="index.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_staff or not self.request.user.is_superuser:
            raise PermissionDenied
        return super(EntryFormView, self).dispatch(*args, **kwargs)
    def get(self,request,*args,**kwargs):
        form = self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form' : form})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.save()
            return HttpResponseRedirect('/')
        return render(request,self.template_name,{'form': form})

class EntryView(ListView):
    model = Entry
    initial = { 'key' : 'value'}
    template_name="base.html"

    def get_context_data(self,**kwargs):
        context = super(EntryView,self).get_context_data(**kwargs)
        context['latest_entry_list'] = Entry.objects.order_by('-pub_date')
        return context

class EntryArchieveAprilView(ListView):
    model = Entry
    initial= {'key' : 'value'}
    template_name="base.html"
    def get_context_data(self,**kwargs):
        context = super(EntryArchieveAprilView,self).get_context_data(**kwargs)
        context['latest_entry_list']= Entry.objects.filter(pub_date__year=2015).filter(pub_date__month=04).order_by('-pub_date')
        return context

class EntryArchieveMarchView(ListView):
    model = Entry
    initial= {'key' : 'value'}
    template_name="base.html"

    def get_context_data(self,**kwargs):
        context = super(EntryArchieveMarchView,self).get_context_data(**kwargs)
        context['latest_entry_list']= Entry.objects.filter(pub_date__year=2015).filter(pub_date__month=03).order_by('-pub_date')
        return context
