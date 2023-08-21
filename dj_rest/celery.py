# -*- coding: utf-8 -*-
import os
from celery import Celery

# Встановіть змінну середовища "DJANGO_SETTINGS_MODULE" для вказання Django на налаштування вашого проекту
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_rest.settings')

# Створіть об'єкт Celery
app = Celery('dj_rest')

# Завантажте налаштування з файлу settings.py проекту
app.config_from_object('django.conf:settings', namespace='CELERY')

# Знайдіть та імпортуйте задачі з файлів tasks.py у вашому додатку
app.autodiscover_tasks()