from django.core.exceptions import ValidationError
from django.forms import ModelForm, CheckboxInput
from django.utils import timezone

from medical.models import Doctor, Appointment, Service, Result, Contact


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, CheckboxInput):
                field.widget.attrs["class"] = "form-control"


class DoctorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"


class ServiceForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Service
        fields = "__all__"


class AppointmentForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Appointment
        exclude = ("owner",)

    def clean_time(self):
        time = self.cleaned_data["time"]
        occupied_time = [
            "23:00",
            "23:30",
            "00:00",
            "00:30",
            "01:00",
            "01:30",
            "02:00",
            "02:30",
            "03:00",
            "03:30",
            "04:00",
            "04:30",
            "05:00",
            "05:30",
            "06:00",
            "06:30",
        ]
        if time in occupied_time:
            raise ValidationError("Это время недоступно для записи")
        return time

    def clean_date(self):
        date = self.cleaned_data["date"]
        current_date = timezone.now().date()
        if date < current_date:
            raise ValidationError("Нельзя указывать дату в прошлом")
        return date


class ResultForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Result
        fields = "__all__"


class ContactForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
