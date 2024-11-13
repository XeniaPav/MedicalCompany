from django.test import TestCase

from medical.models import Doctor, Service, Appointment, Result
from users.models import User


class DoctorTestCase(TestCase):
    """тестирование модели Doctor"""

    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
        self.doctor = Doctor.objects.create(
            name="Иванов Иван Иванович", specialization="Терапевт"
        )

    def test_doctor_detail(self):
        doctor = Doctor.objects.get(name="Иванов Иван Иванович")
        self.assertEqual(doctor.specialization, "Терапевт")

    def test_doctor_list(self):
        doctors_count = Doctor.objects.all().count()
        self.assertEqual(doctors_count, 1)

    def test_doctor_update(self):
        doctor = Doctor.objects.get(name="Иванов Иван Иванович")
        doctor.specialization = "Хирург"
        self.assertEqual(doctor.specialization, "Хирург")

    def test_doctor_create(self):
        Doctor.objects.create(name="Петров Петр Петрович", specialization="ЛОР")
        doctors_count = Doctor.objects.all().count()
        self.assertEqual(doctors_count, 2)

    def test_doctor_delete(self):
        doctor = Doctor.objects.get(name="Иванов Иван Иванович")
        doctor.delete()
        doctors_count = Doctor.objects.all().count()
        self.assertEqual(doctors_count, 0)


class ServiceTestCase(TestCase):
    """тестирование модели Service"""

    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
        self.service = Service.objects.create(service_name="Анализ крови", price=5000)

    def test_service_detail(self):
        service = Service.objects.get(service_name="Анализ крови")
        self.assertEqual(service.price, 5000)

    def test_service_list(self):
        services_count = Service.objects.all().count()
        self.assertEqual(services_count, 1)

    def test_service_update(self):
        service = Service.objects.get(service_name="Анализ крови")
        service.price = 1500
        self.assertEqual(service.price, 1500)

    def test_service_create(self):
        self.service = Service.objects.create(service_name="Биопсия", price=5000)
        services_count = Service.objects.all().count()
        self.assertEqual(services_count, 2)

    def test_service_delete(self):
        service = Service.objects.get(service_name="Анализ крови")
        service.delete()
        services_count = Service.objects.all().count()
        self.assertEqual(services_count, 0)


class AppointmentTestCase(TestCase):
    """тестирование модели Appointment"""

    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
        self.doctor = Doctor.objects.create(
            name="Иванов Иван Иванович", specialization="Терапевт"
        )
        self.appointment = Appointment.objects.create(
            date="2024-10-25", time="10:00", doctor=self.doctor, owner=self.user
        )

    def test_appointment_detail(self):
        appointment = Appointment.objects.get(owner=self.user)
        self.assertEqual(appointment.doctor.name, "Иванов Иван Иванович")

    def test_appointment_list(self):
        appointment_count = Appointment.objects.all().count()
        self.assertEqual(appointment_count, 1)

    def test_appointment_update(self):
        appointment = Appointment.objects.get(owner=self.user)
        appointment.doctor.name = "Петров Петр Петрович"
        self.assertEqual(appointment.doctor.name, "Петров Петр Петрович")

    def test_appointment_create(self):
        self.appointment = Appointment.objects.create(
            date="2024-11-30", time="12:00", doctor=self.doctor, owner=self.user
        )

        appointment_count = Appointment.objects.all().count()
        self.assertEqual(appointment_count, 2)

    def test_appointment_delete(self):
        appointment = Appointment.objects.get(owner=self.user)
        appointment.delete()
        appointment_count = Appointment.objects.all().count()
        self.assertEqual(appointment_count, 0)


class ResultTestCase(TestCase):
    """тестирование модели Result"""

    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
        self.result = Result.objects.create(test="УЗИ", date="2024-11-10", result="ОК")

    def test_result_detail(self):
        result = Result.objects.get(test="УЗИ")
        self.assertEqual(result.result, "ОК")

    def test_result_list(self):
        results_count = Result.objects.all().count()
        self.assertEqual(results_count, 1)

    def test_result_update(self):
        result = Result.objects.get(test="УЗИ")
        result.result = "не ОК"
        self.assertEqual(result.result, "не ОК")

    def test_result_create(self):
        self.result = Result.objects.create(
            test="Анализ", date="2024-11-20", result="специфический"
        )
        results_count = Result.objects.all().count()
        self.assertEqual(results_count, 2)

    def test_result_delete(self):
        result = Result.objects.get(test="УЗИ")
        result.delete()
        results_count = Result.objects.all().count()
        self.assertEqual(results_count, 0)
