from django.contrib import admin

from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    """
    ModelAdmin Class for Todo Model.
    """
    # Change the display order of the Model fields
    list_display = ('title', 'description', 'date_added', 'completed')


admin.site.register(Todo, TodoAdmin)
