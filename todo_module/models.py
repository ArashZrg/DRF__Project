from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    priority = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return f'{self.title} / Is Done: {self.is_done}'

    class Meta:
        db_table = 'todos'
