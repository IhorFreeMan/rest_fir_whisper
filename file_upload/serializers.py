# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import UploadedFile
import whisper


class UploadedFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadedFile
        fields = ('id', 'audio_file', 'uploaded_at', 'text_result')
        read_only_fields = ('id',)

    audio_file = serializers.FileField()

    def process_audio(self, audio_file_path):
        model = whisper.load_model("base")
        result = model.transcribe(audio_file_path[1:], fp16=False)
        text_result = result["text"]

        return text_result

    def update(self, instance, validated_data):
        if 'audio_file' in validated_data:
            audio_file = validated_data['audio_file']
            instance.text_result = self.process_audio(audio_file)

        instance.save()
        return instance