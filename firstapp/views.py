from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext,loader
from .models import Comments
from .forms import CommentCreateForm
from django.core.urlresolvers import reverse
from django.views.generic import ListView
import datetime


class CommentsFormView(ListView):
    form_class= CommentCreateForm
    initial= { 'key': 'value'}
    template_name = '/home/tolga856/newproject/myblog/templates/base.html'

    def get(self,request,*args,**kwargs):
        form = self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form' : form})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.save()
            return HttpResponseRedirect('/base/result/')
        return render(request,self.template_name,{'form': form})

class CommentsView(ListView):
    model = Comments
    initial = { 'key' : 'value'}
    template_name = '/home/tolga856/newproject/myblog/templates/base.html'

    def get_context_data(self,**kwargs):
        context = super(CommentsView,self).get_context_data(**kwargs)
        context['latest_comment_list'] = Comments.objects.order_by('-pub_date')
        return context

class CommentsArchieveAprilView(ListView):
    model = Comments
    initial= {'key' : 'value'}
    template_name = '/home/tolga856/newproject/myblog/templates/base.html'

    def get_context_data(self,**kwargs):
        context = super(CommentsArchieveAprilView,self).get_context_data(**kwargs)
        context['latest_comment_list']= Comments.objects.filter(pub_date__year=2015).filter(pub_date__month=04)

        return context

class CommentsArchieveMarchView(ListView):
    model = Comments
    initial= {'key' : 'value'}
    template_name = 'base.html'

    def get_context_data(self,**kwargs):
        context = super(CommentsArchieveMarchView,self).get_context_data(**kwargs)
        context['latest_comment_list']= Comments.objects.filter(pub_date__year=2015).filter(pub_date__month=03)

        return context
