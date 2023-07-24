from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from .models import UploadedFile
from .serializers import UploadedFileSerializer
import whisper




class AudioFileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        audio_file_serializer = UploadedFileSerializer(data=request.data)
        if audio_file_serializer.is_valid():
            audio_file_serializer.save()
            print(audio_file_serializer.data)

            # Process the audio file using "whisper" module and get the text result
            audio_file_path = audio_file_serializer.data['audio_file']
            text_result = self.process_audio(audio_file_path)

            # Update the 'text_result' field in the database
            UploadedFile.objects.filter(id=audio_file_serializer.data['id']).update(text_result=text_result)

            # Get the updated object from the database
            updated_file = UploadedFile.objects.get(id=audio_file_serializer.data['id'])

            # Serialize the updated object
            audio_file_serializer = UploadedFileSerializer(instance=updated_file)

            return Response(audio_file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(audio_file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def process_audio(self, audio_file_path):
        model = whisper.load_model("base")
        result = model.transcribe(audio_file_path[1:], fp16=False)
        text_result = result["text"]

        return text_result