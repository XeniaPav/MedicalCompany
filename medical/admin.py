from django.contrib import admin

from medical.models import Doctor, Service, Appointment, Result, Static


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "specialization", "qualification", "experience")
    list_filter = ("specialization",)
    search_fields = ("name",)


@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ("id", "service_name", "price")
    list_filter = ("price",)
    search_fields = ("service_name",)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "time", "doctor", "owner")
    list_filter = ("date",)


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "date",
        "test",
        "result",
        "units_of_measurement",
        "reference_values",
    )
    list_filter = ("date",)
    search_fields = ("test",)


@admin.register(Static)
class StaticAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
    )
