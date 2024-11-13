from django.core.cache import cache

from config.settings import CACHE_ENABLED
from medical.models import Doctor


def get_doctors_from_cache():
    """
    Получение списка врачей из кэша. Если кэш пуст,то получение из БД.
    """
    if not CACHE_ENABLED:
        return Doctor.objects.all()
    else:
        key = "doctors_list"
        doctors = cache.get(key)
        if doctors is not None:
            return doctors
        else:
            doctors = Doctor.objects.all()
            cache.set(key, doctors)
            return doctors
