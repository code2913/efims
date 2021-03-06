from django.shortcuts import render
from django.views.generic import CreateView,DetailView,ListView,DeleteView,UpdateView,RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Ballistic,BallisticReport
from . forms import BallisticForm,BallisticReportForm
from django.shortcuts import get_object_or_404
# Create your views here.

class CreateCase(LoginRequiredMixin,CreateView):
    form_class = BallisticForm
    model = Ballistic
    template_name = "ballistic/create.html"

    def form_valid(self, form):
        form.instance.receicer = self.request.user
        return super().form_valid(form)

class BallisticDetailView(LoginRequiredMixin,DetailView):
    model = Ballistic
    object_context_name = "ballistic"
    template_name = "ballistic/detail.html"

    
    def get_context_data(self, **kwargs):
        context = super(BallisticDetailView, self).get_context_data(**kwargs)
        context['form'] = BallisticReportForm
        context['report'] = BallisticReport.objects.filter(case=self.get_object())
        return context

    def get_initial(self):
        return {'case':self.object.pk,'approved':self.request.user}

class ReportCreate(CreateView):
    model = BallisticReport
    form_class = BallisticReportForm

    def get_success_url(self):
        from django.urls import reverse
        return reverse('ballistic:details',kwargs={'pk': self.object.case.pk})

    def form_valid(self, form):
        form.instance.approved = self.request.user
        return super().form_valid(form)
    

class BallisticListView(LoginRequiredMixin,ListView):
    context_object_name = 'cases'
    model = Ballistic
    template_name = "ballistic/list.html"


class BallisticDeleteView(DeleteView):
    model = Ballistic
    success_url = "/ballistic"
    template_name = "ballistic/delete.html"

class BallisticUpdate(UpdateView):
    form_class = BallisticForm
    model = Ballistic
    template_name = "ballistic/update.html"

class ApproveBallistc(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'ballistic:details'

    def get_redirect_url(self, *args, **kwargs):
        report = get_object_or_404(BallisticReport, case=kwargs['pk'])
        # report = BallisticReport.objects.get(case=kwargs['pk'])
        report.approve = True
        report.approved = self.request.user
        report.save()
        # report.update(approve=True,reported_by=self.request.user)
        return super().get_redirect_url(*args, **kwargs)