from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.views import logout
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from django.contrib import auth
from django.core.context_processors import csrf
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from .models import Entry
from .forms import EntryCreateForm, EntryUpdateForm


def custom_login(request, *args, **kwargs):
    c = {}
    c.update(csrf(request))
    messages.success(request,"You are successfully logged in")
    return render_to_response('post/login.html', c)

def custom_logout(request):
    logout(request)
    messages.success(
        request, "You have logged out successfully.")
    return HttpResponseRedirect("/")

def auth_view(request):
    username = request.POST.get('username' , '')
    password = request.POST.get('password' , '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
       auth.login(request, user)
       return HttpResponseRedirect("/")
    else:
       return HttpResponseRedirect("login/")


class EntryCreateView(CreateView):
    model = Entry
    form_class = EntryCreateForm
    template_name = "post/entry_create.html"
    success_url = reverse_lazy("index")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EntryCreateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form' : form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid() and not Entry.objects.all().filter(title=form.instance.title):
            instance = form.instance
            instance.author = self.request.user
            instance.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(self.request, "Invalid title")
            return HttpResponseRedirect("")
        return render(request, self.template_name, {'form' : form})


class EntryView(ListView):
    model = Entry
    initial = {'key' : 'value'}
    template_name="post/entry_list.html"

    def get_context_data(self,**kwargs):
        context = super(EntryView, self).get_context_data(**kwargs)
        context['latest_entry_list'] = Entry.objects.order_by('-pub_date')
        return context


class EntryDetailView(DetailView):
    model = Entry
    template_name= "post/entry_detail.html"


class EntryUpdateView(UpdateView):
    model = Entry
    form_class = EntryUpdateForm
    template_name = 'post/entry_update.html'
    success_url = reverse_lazy("base")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if self.request.user != self.get_object().author:
            raise PermissionDenied
        return super(EntryUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        if not Entry.objects.all().filter(title=form.instance.title):
            return super(EntryUpdateView, self).form_valid(form)
        else:
            messages.error(self.request, "Invalid title")
            return HttpResponseRedirect("")



class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy('base')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if self.request.user != self.get_object().author:
            raise PermissionDenied
        return super(EntryDeleteView, self).dispatch(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(EntryDeleteView, self).delete(request, *args, **kwargs)
