from django.shortcuts import render
from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView,RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import BiologyPF180,PoliceForm113,BiologyPF180Report,PoliceForm113Report
from . forms import BiologyPF180Form, Police113form,BiologyPF180ReportForm,Police113ReportForm
from django.shortcuts import get_object_or_404



# Create your views here.

class BiologyListView(LoginRequiredMixin,ListView):
    model = BiologyPF180
    context_object_name = "dna"
    template_name = "dna/biology-list.html"

class BiologyDetail(LoginRequiredMixin,DetailView):
    model = BiologyPF180
    context_object_name = 'dna'
    template_name = "dna/biology-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BiologyPF180ReportForm
        context['report'] = BiologyPF180Report.objects.filter(case=self.get_object())
        return context
    

class BiologyCreate(LoginRequiredMixin,CreateView):
    model = BiologyPF180
    form_class = BiologyPF180Form
    template_name = "dna/create.html"


class BiologyUpdateView(UpdateView):
    form_class = BiologyPF180Form
    model = BiologyPF180
    template_name = "dna/updatepf180.html"


class BiologyDeleteView(DeleteView):
    success_url = "/dna/biology"
    model = BiologyPF180
    template_name = "dna/deletepf180.html"


# form 113 police

class Policeform113List(LoginRequiredMixin,ListView):
    model = PoliceForm113
    context_object_name = "dna"
    template_name = "dna/police113-list.html"


class Policeform113Detail(LoginRequiredMixin,DetailView):
    model = PoliceForm113
    context_object_name = "dna"
    template_name = "dna/police113-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = Police113ReportForm
        context['report'] = PoliceForm113Report.objects.filter(case=self.get_object())
        return context


class PoliceForm113Create(LoginRequiredMixin,CreateView):
    model = PoliceForm113
    form_class = Police113form
    template_name = "dna/police113-create.html"

class PoliceFormUpdateView(LoginRequiredMixin,UpdateView):
    form_class = Police113form
    model = PoliceForm113
    template_name = "dna/updatepf180.html"


class PoliceFormDeleteView(LoginRequiredMixin,DeleteView):
    success_url = "dna/police113"
    model = PoliceForm113
    template_name = "dna/deletepf180.html"

class ReportCreate113(LoginRequiredMixin,CreateView):
    model = PoliceForm113Report
    form_class = Police113ReportForm

    def get_success_url(self):
        from django.urls import reverse
        return reverse('dna:police-detail',kwargs={'pk': self.object.case.pk})

    def form_valid(self, form):
        form.instance.approved = self.request.user
        return super().form_valid(form)

class ReportCreate180(LoginRequiredMixin,CreateView):
    model = BiologyPF180Report
    form_class = BiologyPF180ReportForm

    def get_success_url(self):
        from django.urls import reverse
        return reverse('dna:detail',kwargs={'pk': self.object.case.pk})

    def form_valid(self, form):
        form.instance.approved = self.request.user
        return super().form_valid(form)

class ApporvePF180(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'dna:detail'

    def get_redirect_url(self, *args, **kwargs):
        report = get_object_or_404(BiologyPF180Report, pk=kwargs['pk'])
        report.approve = True
        report.approved = self.request.user
        report.save()
        return super().get_redirect_url(*args, **kwargs)



class ApprovePolice113(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'dna:police-detail'

    def get_redirect_url(self, *args, **kwargs):
        report = get_object_or_404(PoliceForm113Report, pk=kwargs['pk'])
        report.update(approve=True,reported_by=self.request.user)
        report.approve = True
        report.approved = self.request.user
        report.save()
        return super().get_redirect_url(*args, **kwargs)