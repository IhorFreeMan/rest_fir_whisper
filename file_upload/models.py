from django.db import models



class UploadedFileManager(models.Manager):
    def update_text_result(self, file_id, text_result):
        """
        Оновлює поле text_result для UploadedFile з заданим ідентифікатором file_id.
        """
        try:
            uploaded_file = self.get(id=file_id)
            uploaded_file.text_result = text_result
            uploaded_file.save()  # Збереження оновленого об'єкту в базі даних
            return uploaded_file
        except UploadedFile.DoesNotExist:
            return None


class UploadedFile(models.Model):
    audio_file = models.FileField(upload_to='uploads/audio/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    text_result = models.TextField(blank=True, null=True)

    objects = UploadedFileManager()  # Встановлення власного менеджера