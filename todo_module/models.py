from django.db import models


# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)

    class Meta:
        db_table = 'todo'
