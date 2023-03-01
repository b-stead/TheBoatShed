from django.db import models


# Create your models here.
class VboData(models.Model):
    file = models.TextField()


    def __str__(self):
        return f'{self.session.crew} {self.session.session_date} {self.session.session}'