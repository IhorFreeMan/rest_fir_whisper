# -*- coding: utf-8 -*-

import whisper
from celery import shared_task
from .models import UploadedFile

@shared_task
def process_audio_task(audio_file_path, file_id):
    model = whisper.load_model("base")
    result = model.transcribe(audio_file_path[1:], fp16=False)
    text_result = result["text"]

    # Оновлюємо поле text_result у базі даних
    try:
        uploaded_file = UploadedFile.objects.get(pk=file_id)
        uploaded_file.text_result = text_result
        uploaded_file.save()
    except UploadedFile.DoesNotExist:
        pass

    return text_result