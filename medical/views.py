from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from medical.forms import (
    DoctorForm,
    ServiceForm,
    AppointmentForm,
    ResultForm,
    ContactForm,
)
from medical.models import Doctor, Service, Appointment, Result, Contact, Static
from medical.services import get_doctors_from_cache


class HomeView(TemplateView):
    """Главная страница сайта"""

    template_name = "medical/index.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        services = Service.objects.all()
        companies = Static.objects.all()
        context_data["random_doctors"] = Doctor.objects.all()
        context_data["random_doctors"] = get_doctors_from_cache().order_by("?")[:3]
        context_data["all_services"] = services.order_by("?")[:3]
        context_data["all_companies"] = companies.order_by()
        return context_data


class CompanyView(TemplateView):
    """Страница  "О компании" """

    template_name = "medical/company.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        services = Service.objects.all()
        companies = Static.objects.all()
        context_data["random_doctors"] = get_doctors_from_cache().order_by("?")[:3]
        context_data["all_services"] = services.order_by("?")[:3]
        context_data["all_companies"] = companies.order_by()
        return context_data


class DoctorListView(ListView):
    """Отображение списка врачей"""

    model = Doctor

    def get_queryset(self):
        return get_doctors_from_cache()


class DoctorDetailView(DetailView):
    """Отображение информации о враче"""

    model = Doctor


class DoctorCreateView(CreateView, LoginRequiredMixin):
    """Создание врача"""

    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy("medical:doctors_list")


class DoctorUpdateView(UpdateView, LoginRequiredMixin):
    """Редактирование врача"""

    model = Doctor
    form_class = DoctorForm

    def get_success_url(self):
        return reverse("medical:doctor_detail", args=[self.kwargs.get("pk")])


class DoctorDeleteView(DeleteView, LoginRequiredMixin):
    """Удаление врача"""

    model = Doctor
    success_url = reverse_lazy("medical:doctors_list")


class ServiceListView(ListView):
    """Список услуг"""

    model = Service


class ServiceDetailView(DetailView):
    """Отображение информации об услуге"""

    model = Service


class ServiceCreateView(CreateView, LoginRequiredMixin):
    """Создание услуги"""

    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy("medical:services_list")


class ServiceUpdateView(UpdateView, LoginRequiredMixin):
    """Редактирование услуги"""

    model = Service
    form_class = ServiceForm

    def get_success_url(self):
        return reverse("medical:service_detail", args=[self.kwargs.get("pk")])


class ServiceDeleteView(DeleteView, LoginRequiredMixin):
    """Удаление услуги"""

    model = Service
    success_url = reverse_lazy("medical:services_list")


class AppointmentListView(ListView, LoginRequiredMixin):
    """Отображение списка записей"""

    model = Appointment

    def get_queryset(self, queryset=None):
        queryset = super().get_queryset()
        user = self.request.user
        if not user.is_superuser and not user.groups.filter(name="moderator"):
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class AppointmentDetailView(DetailView, LoginRequiredMixin):
    """Отображение информации о записи"""

    model = Appointment


class AppointmentCreateView(CreateView, LoginRequiredMixin):
    """Создание записи"""

    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy("medical:appointments_list")

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.owner = user
        mailing.save()
        return super().form_valid(form)


class AppointmentUpdateView(UpdateView, LoginRequiredMixin):
    """Редактирование записи"""

    model = Appointment
    form_class = AppointmentForm

    def get_success_url(self):
        return reverse("medical:appointment_detail", args=[self.kwargs.get("pk")])


class AppointmentDeleteView(DeleteView, LoginRequiredMixin):
    """Удаление записи"""

    model = Appointment
    success_url = reverse_lazy("medical:appointments_list")


class ResultListView(ListView, LoginRequiredMixin):
    """Отображение списка результатов"""

    model = Result

    def get_queryset(self, queryset=None):
        queryset = super().get_queryset()
        user = self.request.user
        if not user.is_superuser and not user.groups.filter(name="moderator"):
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class ResultCreateView(CreateView):
    """Создание результата"""

    model = Result
    form_class = ResultForm
    success_url = reverse_lazy("medical:results_list")


class ResultUpdateView(UpdateView):
    """Редактирование результата"""

    model = Result
    form_class = ResultForm
    success_url = reverse_lazy("medical:results_list")


class ResultDeleteView(DeleteView):
    """Удаление записи"""

    model = Result
    success_url = reverse_lazy("medical:appointments_list")


class ContactCreateView(CreateView):
    """Создание сообщения"""

    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy("medical:contacts")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        companies = Static.objects.all()
        context_data["all_companies"] = companies.order_by()
        return context_data
