from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from .models import UploadedFile
from .serializers import UploadedFileSerializer
import whisper




from .tasks import process_audio_task

class AudioFileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        audio_file_serializer = UploadedFileSerializer(data=request.data)
        if audio_file_serializer.is_valid():
            audio_file_serializer.save()

            # Process the audio file asynchronously using Celery
            audio_file_path = audio_file_serializer.data['audio_file']
            file_id = audio_file_serializer.data['id']
            process_audio_task.delay(audio_file_path, file_id)

            return Response(audio_file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(audio_file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AudioFileStatusView(APIView):
    def get(self, request, *args, **kwargs):
        file_id = kwargs['file_id']
        try:
            uploaded_file = UploadedFile.objects.get(pk=file_id)
            if uploaded_file.text_result:
                # Якщо результат обробки доступний, повертаємо текст
                return Response({'status': 'processed', 'text_result': uploaded_file.text_result})
            else:
                # Якщо результат обробки ще не готовий, повертаємо статус "processing"
                return Response({'status': 'processing'})
        except UploadedFile.DoesNotExist:
            return Response({'status': 'not_found'}, status=status.HTTP_404_NOT_FOUND)