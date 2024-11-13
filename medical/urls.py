from django.urls import path
from django.views.decorators.cache import cache_page

from medical.apps import MedicalConfig
from medical.views import (
    HomeView,
    DoctorListView,
    DoctorDetailView,
    DoctorCreateView,
    DoctorUpdateView,
    DoctorDeleteView,
    ServiceListView,
    ServiceDetailView,
    ServiceCreateView,
    ServiceUpdateView,
    ServiceDeleteView,
    AppointmentListView,
    AppointmentDetailView,
    AppointmentCreateView,
    AppointmentUpdateView,
    AppointmentDeleteView,
    ResultListView,
    ResultCreateView,
    ResultUpdateView,
    ResultDeleteView,
    ContactCreateView,
    CompanyView,
)

app_name = MedicalConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("company/", CompanyView.as_view(), name="company"),
    path("contacts/", ContactCreateView.as_view(), name="contacts"),
    path("doctors_list/", DoctorListView.as_view(), name="doctors_list"),
    path(
        "doctor/<int:pk>/",
        cache_page(60)(DoctorDetailView.as_view()),
        name="doctor_detail",
    ),
    path("doctor_create/", DoctorCreateView.as_view(), name="doctor_create"),
    path("doctor_edit/<int:pk>/", DoctorUpdateView.as_view(), name="doctor_edit"),
    path("doctor_delete/<int:pk>/", DoctorDeleteView.as_view(), name="doctor_delete"),
    path("services_list/", ServiceListView.as_view(), name="services_list"),
    path(
        "service/<int:pk>/",
        cache_page(60)(DoctorDetailView.as_view()),
        name="service_detail",
    ),
    path("service_create/", ServiceCreateView.as_view(), name="service_create"),
    path("service_edit/<int:pk>/", ServiceUpdateView.as_view(), name="service_edit"),
    path(
        "service_delete/<int:pk>/", ServiceDeleteView.as_view(), name="service_delete"
    ),
    path("appointments_list/", AppointmentListView.as_view(), name="appointments_list"),
    path(
        "appointment/<int:pk>/",
        cache_page(60)(DoctorDetailView.as_view()),
        name="appointment_detail",
    ),
    path(
        "appointment_create/",
        AppointmentCreateView.as_view(),
        name="appointment_create",
    ),
    path(
        "appointment_edit/<int:pk>/",
        AppointmentUpdateView.as_view(),
        name="appointment_edit",
    ),
    path(
        "appointment_delete/<int:pk>/",
        AppointmentDeleteView.as_view(),
        name="appointment_delete",
    ),
    path("results_list/", ResultListView.as_view(), name="results_list"),
    path("result_create/", ResultCreateView.as_view(), name="result_create"),
    path("result_edit/<int:pk>/", ResultUpdateView.as_view(), name="result_edit"),
    path("result_delete/<int:pk>/", ResultDeleteView.as_view(), name="result_delete"),
]
