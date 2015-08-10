from django.contrib import admin
from .models import Category, Achievement


class CategoryAdmin(admin.ModelAdmin):
    pass

class AchievementAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Achievement, AchievementAdmin)
