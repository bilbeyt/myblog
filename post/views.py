from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext,loader
from .models import Entry
from .forms import EntryCreateForm
from django.core.urlresolvers import reverse
from django.views.generic import ListView
import datetime


class EntryFormView(ListView):
    form_class= EntryCreateForm
    initial= { 'key': 'value'}
    template_name = '/home/tolga856/project/myblog/templates/base.html'

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
    template_name = '/home/tolga856/project/myblog/templates/base.html'

    def get_context_data(self,**kwargs):
        context = super(EntryView,self).get_context_data(**kwargs)
        context['latest_entry_list'] = Entry.objects.order_by('-pub_date')
        return context

class EntryArchieveAprilView(ListView):
    model = Entry
    initial= {'key' : 'value'}
    template_name = '/home/tolga856/project/myblog/templates/base.html'

    def get_context_data(self,**kwargs):
        context = super(EntryArchieveAprilView,self).get_context_data(**kwargs)
        context['latest_entry_list']= Entry.objects.filter(pub_date__year=2015).filter(pub_date__month=04)

        return context

class EntryArchieveMarchView(ListView):
    model = Entry
    initial= {'key' : 'value'}
    template_name = '/home/tolga856/project/myblog/templates/base.html'

    def get_context_data(self,**kwargs):
        context = super(EntryArchieveMarchView,self).get_context_data(**kwargs)
        context['latest_entry_list']= Entry.objects.filter(pub_date__year=2015).filter(pub_date__month=03)

        return context
