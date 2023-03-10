from django.db import models
from django.conf import settings
    
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<user_name>/<filename>
    return '{0}/{1}'.format(instance.owner.user_name, filename)

class Vbo(models.Model):
    file = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    session_date = models.DateField(null=True)
    crew = models.CharField(max_length=20)
    session = models.CharField(max_length=50)
    processed = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.crew} {self.session_date}'

    def formatted_date(self):
        return self.session_date.strftime('%d/%m/%Y')
