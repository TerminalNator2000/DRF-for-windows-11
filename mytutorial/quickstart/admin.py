from django.contrib import admin
from .models import YourModel  # Replace with your actual model(s)

@admin.register(YourModel)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Customize fields
