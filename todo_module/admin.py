from django.contrib import admin

from todo_module.models import Todo


# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass
