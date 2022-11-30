from django.db import models
from django.db.models.fields.files import FileField
from django.contrib.auth.models import User

# Create your models here.
class Upload_Emails(models.Model):

    class Meta:
        verbose_name = 'Upload Emails'
        verbose_name_plural = 'Upload Emails'

    title   = models.CharField(max_length=50)
    email   = FileField(upload_to='Email_Uploads', null=False)
    remarks = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


# # Select whichever user you want to (any of these work)
# user = User.objects.get(username='admin')
# user = User.objects.get(id=64)
# user = request.user

# # Then filter by that user
# user_games = Game.objects.filter(owner=user)